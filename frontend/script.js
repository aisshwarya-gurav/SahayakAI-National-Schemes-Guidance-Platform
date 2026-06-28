const chatBox = document.getElementById("chatBox");
const input = document.getElementById("userInput");

let schemes = [];

// ---------------------------
// Welcome Message
// ---------------------------
window.onload = () => {
    addMessage(`
        <h3>👋 Welcome to <b>Sahayak AI</b></h3>

        <p>
        Tell me about yourself naturally.
        </p>

    `);
};

// ---------------------------
// Add Chat Message
// ---------------------------
function addMessage(html, sender = "bot") {

    const div = document.createElement("div");

    div.className = "message " + sender;

    if (sender === "bot") {

        div.innerHTML = `
        <div class="bot-avatar">🤖</div>

        <div class="bubble">
            ${html}
        </div>
        `;

    } else {

        div.innerHTML = `
        <div class="bubble">
            ${html}
        </div>
        `;

    }

    chatBox.appendChild(div);

    chatBox.scrollTop = chatBox.scrollHeight;

}

// ---------------------------
// Typing Animation
// ---------------------------
function showTyping() {

    const typing = document.createElement("div");

    typing.className = "message bot";

    typing.id = "typing";

    typing.innerHTML = `
    <div class="bot-avatar">🤖</div>

    <div class="bubble">

        <div class="typing">
            <span></span>
            <span></span>
            <span></span>
        </div>

    </div>
    `;

    chatBox.appendChild(typing);

    chatBox.scrollTop = chatBox.scrollHeight;

}

function removeTyping() {

    const t = document.getElementById("typing");

    if (t) t.remove();

}

// ---------------------------
// Send Message
// ---------------------------
async function sendMessage() {

    const query = input.value.trim();

    if (query === "") return;

    addMessage(query, "user");

    input.value = "";

    showTyping();

    try {

        // Temporary profile
        const profile = {

            message: query

        };

        const response = await fetch("http://127.0.0.1:8000/recommend",{

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify(profile)

        });

        const data = await response.json();

        removeTyping();

        schemes = data.matched_schemes || data.recommendations || [];

        if(schemes.length===0){

            addMessage("❌ No schemes found.");

            return;

        }

        let html = `
        <h3>🎉 I found <b>${schemes.length}</b> schemes for you.</h3>
        <br>
        `;

        schemes.forEach((scheme,index)=>{

            html += `
            <div class="scheme-card">

                <h2>${scheme.name}</h2>

                <p><b>Category:</b> ${scheme.category}</p>

                <p>
                ${(scheme.description || "").substring(0,170)}...
                </p>

                <button
                    class="know-btn"
                    onclick="showScheme(${index})">

                    Know More →

                </button>

            </div>
            `;

        });

        addMessage(html);

    }

    catch(err){

        removeTyping();

        addMessage("❌ Unable to connect to backend.");

        console.log(err);

    }

}

// ---------------------------
// Know More
// ---------------------------
function showScheme(index){

    const scheme = schemes[index];

    addMessage(`Tell me more about <b>${scheme.name}</b>`,"user");

    addMessage(`

    <div class="scheme-card">

        <h2>${scheme.name}</h2>

        <p>${scheme.description || ""}</p>

        <br>

        <p><b>Category:</b> ${scheme.category || ""}</p>

        <p><b>Ministry:</b> ${scheme.ministry || ""}</p>

        <p><b>Launch Year:</b> ${scheme.launch_year || ""}</p>

        <h4>🎁 Benefits</h4>

        <ul>

        ${(scheme.benefits || []).map(x=>`<li>${x}</li>`).join("")}

        </ul>

        <h4>📄 Required Documents</h4>

        <ul>

        ${(scheme.required_documents || []).map(x=>`<li>${x}</li>`).join("")}

        </ul>

        <h4>📝 How to Apply</h4>

        <ol>

        ${(scheme.application_process || []).map(x=>`<li>${x}</li>`).join("")}

        </ol>

        <a
            href="${scheme.official_website || '#'}"
            target="_blank">

            🌐 Visit Official Website

        </a>

    </div>

    `);

}

// ---------------------------
// Enter Key
// ---------------------------
input.addEventListener("keydown",function(e){

    if(e.key==="Enter"){

        e.preventDefault();

        sendMessage();

    }

});

