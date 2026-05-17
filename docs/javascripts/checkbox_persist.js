/* 
 * Persistent Checkboxes via Gitea API
 * Intercepts MkDocs Material checkbox clicks and commits changes back to Gitea
 * Place in docs/javascripts/checkbox_persist.js
 * Add to mkdocs.yml: extra_javascript: [javascripts/checkbox_persist.js]
 */

const GITEA_URL = 'http://192.168.1.3:3000';
const GITEA_TOKEN = '0e5e0aed245d193f3d0701c40ab4b4ab01711312';
const GITEA_OWNER = 'cos';
const GITEA_REPO = 'mkdocs_dev_material'; // update if repo name differs
const DOCS_PATH = 'docs/';

// Get the current page's markdown file path from the URL
function getMarkdownPath() {
    const path = window.location.pathname;
    // Strip leading slash and trailing slash/index.html
    let page = path.replace(/^\//, '').replace(/\/$/, '').replace(/\/index$/, '');
    // If empty, it's the index page
    if (!page) page = 'index';
    // Remove any .html extension
    page = page.replace(/\.html$/, '');
    return DOCS_PATH + page + '.md';
}

// Fetch file content and SHA from Gitea
async function getFileFromGitea(filePath) {
    const url = `${GITEA_URL}/api/v1/repos/${GITEA_OWNER}/${GITEA_REPO}/contents/${filePath}`;
    const resp = await fetch(url, {
        headers: { 'Authorization': `token ${GITEA_TOKEN}` }
    });
    if (!resp.ok) throw new Error(`Gitea fetch failed: ${resp.status}`);
    const data = await resp.json();
    return {
        sha: data.sha,
        content: atob(data.content.replace(/\n/g, ''))
    };
}

// Commit updated content back to Gitea
async function putFileToGitea(filePath, sha, content, message) {
    const url = `${GITEA_URL}/api/v1/repos/${GITEA_OWNER}/${GITEA_REPO}/contents/${filePath}`;
    const resp = await fetch(url, {
        method: 'PUT',
        headers: {
            'Authorization': `token ${GITEA_TOKEN}`,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            message,
            content: btoa(unescape(encodeURIComponent(content))),
            sha
        })
    });
    if (!resp.ok) throw new Error(`Gitea PUT failed: ${resp.status}`);
    return resp.json();
}

// Toggle the nth checkbox in the markdown content
function toggleCheckboxInMarkdown(content, index, checked) {
    let count = 0;
    return content.replace(/- \[(x| )\]/g, (match) => {
        if (count === index) {
            count++;
            return checked ? '- [x]' : '- [ ]';
        }
        count++;
        return match;
    });
}

// Get the index of a checkbox element among all checkboxes on the page
function getCheckboxIndex(checkbox) {
    const all = document.querySelectorAll('.md-content input[type="checkbox"]');
    return Array.from(all).indexOf(checkbox);
}

// Main handler
async function handleCheckboxClick(event) {
    const checkbox = event.target;
    const checked = checkbox.checked;
    const index = getCheckboxIndex(checkbox);
    const filePath = getMarkdownPath();

    // Show a subtle saving indicator
    checkbox.disabled = true;
    const label = checkbox.closest('li');
    if (label) label.style.opacity = '0.6';

    try {
        const { sha, content } = await getFileFromGitea(filePath);
        const updated = toggleCheckboxInMarkdown(content, index, checked);
        const verb = checked ? 'Check' : 'Uncheck';
        await putFileToGitea(filePath, sha, updated, `${verb} todo item via MkDocs`);
        // Success — re-enable
        checkbox.disabled = false;
        if (label) label.style.opacity = '1';
    } catch (err) {
        console.error('Failed to save checkbox state:', err);
        // Revert the checkbox if save failed
        checkbox.checked = !checked;
        checkbox.disabled = false;
        if (label) label.style.opacity = '1';
    }
}

// Attach listeners after DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    const checkboxes = document.querySelectorAll('.md-content input[type="checkbox"]');
    checkboxes.forEach(cb => {
        cb.addEventListener('change', handleCheckboxClick);
    });
});
