const apiUrl = "http://localhost:8888/memos";

let editingMemoId = null;

function displayMessage(message) {
    alert(message);
}

function resetForm() {
    document.getElementById("formTitle").textContent = "メモの作成";
    document.getElementById("title").value = "";
    document.getElementById("description").value = "";
    document.getElementById("updateButton").style.display = "none";
    document.querySelector("#createMemoForm button[type='submit']").style.display = "block";
    editingMemoId = null;
}

async function creteMemo(memo) {
    try {
        const response = await fetch(apiUrl, {
            method: "POST",
            headers: {'content-type': 'application/json'},
            body: JSON.stringify(memo)
        });
        const data = await response.json();
        if (response.ok) {
            displayMessage(data.message);
            resetForm();
            await fechAndDisplayMemos();
        } else {
            if (response.status === 422) {
                displayMessage('入力内容に誤りがあります。');
            } else {
                displayMessage(data.detail);
            }
        } 
    } catch (error) {
        console.error('メモ作成中にエラーが発生しました:', error);
    }
}

async function updateMemo(memo) {
    try{
        const response = await fetch(`${apiUrl}/${editingMemoId}`, {
            method: "PUT",
            headers: {'content-type': 'application/json'},
            body: JSON.stringify(memo)
        });
        const data = await response.json();
        if (response.ok) {
            displayMessage(data.message);
            resetForm();
            await fechAndDisplayMemos();
        } else {
            if (response.status === 422) {
                displayMessage('入力内容に誤りがあります。');
            } else {
                displayMessage(data.detail);
            }
        } 
    } catch (error) {
        console.error('メモ更新中にエラーが発生しました:', error);
    }
}

async function deleteMemo(memoId) {
    try {
        const response = await fetch(`${apiUrl}/${memoId}`, {
            method: "DELETE"
        });
        const data = await response.json();
        if (response.ok) {
            displayMessage(data.message);
            await fechAndDisplayMemos();
        } else {
            displayMessage(data.detail);
        } 
    } catch (error) {
        console.error('メモ削除中にエラーが発生しました:', error);
    }
}

async function fechAndDisplayMemos() {
    try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const memos = await response.json();
        const memoTableBody = document.querySelector('#memos tbody');

        memoTableBody.innerHTML = '';
        memos.forEach(memo => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${memo.title}</td>
                <td>${memo.description}</td>
                <td>
                    <button class="edit-button" data-memo-id="${memo.id}">編集</button>
                    <button class="delete-button" data-memo-id="${memo.id}">削除</button>
                </td>
            `;
            memoTableBody.appendChild(row);
        });
    } catch (error) {
        console.error('メモ一覧の取得中にエラーが発生しました:', error);
    }
}

async function editMemo(memoId) {
    editingMemoId = memoId;
    const response = await fetch(`${apiUrl}/${memoId}`);
    const memo = await response.json();
    if (response.ok) {
        await displayMessage(memo.detail);
        return;
    }
    document.getElementById('title').value = memo.title;
    document.getElementById('description').value = memo.description;
    document.getElementById("formTitle").textContent = "メモの編集";
    document.getElementById("updateButton").style.display = "block";
    document.querySelector("#createMemoForm button[type='submit']").style.display = "none";
}

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('createMemoForm');

    form.onsubmit = async (event) => {
        event.preventDefault();
        const title = document.getElementById('title').value;
        const description = document.getElementById('description').value;
        const memo = { title, description };
        if (editingMemoId) {
            await updateMemo(memo);
        } else {
            await creteMemo(memo);
        }
    };

    document.getElementById('updateButton').onclick = async () => {
        const title = document.getElementById('title').value;
        const description = document.getElementById('description').value;
        const memo = { title, description };
        await updateMemo(memo);
    };

    document.querySelector('#memos tbody').addEventListener('click', async (event) => {
        if (event.target.className === 'edit') {
            const memoId = event.target.dataset.id;
            await editMemo(memoId);
        } else if (event.target.className === 'delete') {
            const memoId = event.target.dataset.id;
            await deleteMemo(memoId);
        }
    });
});

document.addEventListener('DOMContentLoaded', fechAndDisplayMemos);