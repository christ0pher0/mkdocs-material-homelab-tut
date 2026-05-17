/*
 * Persistent Checkboxes via Gitea API
 */
const GITEA_URL = 'http://192.168.1.3:3000';
const GITEA_TOKEN = 'e54707633fc7d1cfa47966a0e64496788715777e';
const GITEA_OWNER = 'cos';
const GITEA_REPO = 'mkdocs_dev_material';
const DOCS_PATH = 'docs/';
const WEBHOOK_URL = 'http://192.168.1.3:9999/webhook';

function getMarkdownPath() {
    const path = window.location.pathname;
    let page = path.replace(/^\//, '').replace(/\/$/, '').replace(/\/index$/, '');
    if (!page) page = 'index';
    page = page.replace(/\.html$/, '');
    return DOCS_PATH + page + '.md';
}

async function getFileFromGitea(filePath) {
    const url = `${GITEA_URL}/api/v1/repos/${GITEA_OWNER}/${GITEA_REPO}/contents/${filePath}`;
    const resp = await fetch(url, { headers: { 'Authorization': `token ${GITEA_TOKEN}` } });
    if (!resp.ok) throw new Error(`Gitea fetch failed: ${resp.status}`);
    const data = await resp.json();
    return {
        sha: data.sha,
        content: decodeURIComponent(escape(atob(data.content.replace(/\n/g, ''))))
    };
}

async function putFileToGitea(filePath, sha, content, message) {
    const url = `${GITEA_URL}/api/v1/repos/${GITEA_OWNER}/${GITEA_REPO}/contents/${filePath}`;
    const resp = await fetch(url, {
        method: 'PUT',
        headers: { 'Authorization': `token ${GITEA_TOKEN}`, 'Content-Type': 'application/json' },
        body: JSON.stringify({
            message,
            content: btoa(unescape(encodeURIComponent(content))),
            sha
        })
    });
    if (!resp.ok) throw new Error(`Gitea PUT failed: ${resp.status}`);
    return resp.json();
}

function toggleCheckboxInMarkdown(content, index, checked) {
    let count = 0;
    return content.replace(/- \[(x| )\]/g, (match) => {
        if (count === index) { count++; return checked ? '- [x]' : '- [ ]'; }
        count++;
        return match;
    });
}

function getCheckboxIndex(checkbox) {
    const all = document.querySelectorAll('.md-typeset .task-list-item input[type="checkbox"]');
    return Array.from(all).indexOf(checkbox);
}

async function handleCheckboxClick(checkbox, newState) {
    const index = getCheckboxIndex(checkbox);
    const filePath = getMarkdownPath();
    console.log(`[CB] index=${index} newState=${newState} filePath=${filePath}`);
    checkbox.disabled = true;
    const li = checkbox.closest('li');
    if (li) li.style.opacity = '0.5';
    try {
        const { sha, content } = await getFileFromGitea(filePath);
        const updated = toggleCheckboxInMarkdown(content, index, newState);
        const verb = newState ? 'Check' : 'Uncheck';
        console.log(`[CB] committing: ${verb} index ${index}`);
        await putFileToGitea(filePath, sha, updated, `${verb} todo item via MkDocs`);
        checkbox.checked = newState;
        console.log(`[CB] done — NOT calling webhook (debug mode)`);
        // await fetch(WEBHOOK_URL, { method: 'POST' }).catch(() => {});  // DISABLED for debug
    } catch (err) {
        console.error('[CB] Failed:', err);
        checkbox.checked = !newState;
    } finally {
        checkbox.disabled = false;
        if (li) li.style.opacity = '1';
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const items = document.querySelectorAll('.md-typeset .task-list-item');
    console.log(`[CB] DOMContentLoaded — found ${items.length} task items`);
    items.forEach((item, i) => {
        const cb = item.querySelector('input[type="checkbox"]');
        if (!cb) return;
        item.style.cursor = 'pointer';
        cb.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            console.log(`[CB] checkbox click — cb.checked=${cb.checked} (before toggle)`);
            const newState = !cb.checked;
            handleCheckboxClick(cb, newState);
        });
        item.addEventListener('click', (e) => {
            if (e.target.type === 'checkbox') return;
            e.preventDefault();
            console.log(`[CB] li click — cb.checked=${cb.checked}`);
            const newState = !cb.checked;
            handleCheckboxClick(cb, newState);
        });
    });
});
