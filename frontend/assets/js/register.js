document.getElementById("registerForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    const full_name = document.getElementById("full_name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const role = document.getElementById("role").value;
    const department_id = document.getElementById("department_id").value;
    const errorMsg = document.getElementById("error");

    const data = {
        full_name: full_name,
        email: email,
        password: password,
        role: role,
        department_id: department_id ? Number(department_id) : null
    };

    const response = await fetch("http://127.0.0.1:8000/api/register", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    if (response.status === 200) {
        const user = await response.json();
        localStorage.setItem("user", JSON.stringify(user));
        errorMsg.textContent = "Kayıt başarılı!";
        errorMsg.style.color = "green";
        window.location.href = "login.html";

    } else {
        const err = await response.json().catch(() => null);
        console.log("Hata:", err);
        errorMsg.textContent = "Kayıt İşlemi Gerçekleştirilemiyor";
    }
});
