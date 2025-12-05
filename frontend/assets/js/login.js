document.getElementById("loginForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();
    const errorMsg = document.getElementById("error");

    try {
        const response = await fetch("http://127.0.0.1:8000/api/login", { // api/login endpointine veri gönderecek
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email, password })
        });

        console.log("Response:", response);

        if (response.status === 200) {
            // Giriş başarılı → kullanıcı verisini al
            const user = await response.json();

            // Kullanıcı bilgilerini localStorage'a kaydet
            localStorage.setItem("user", JSON.stringify(user));

            // Dashboard'a gönder
            window.location.href = "dashboard.html";

        } else {

            let err = "";
            try {
                const errorData = await response.json();
                err = errorData.detail || "E-posta veya şifre hatalı.";
            } catch {
                err = "E-posta veya şifre hatalı.";
            }
            errorMsg.textContent = err;
        }
    } catch (err) {
        console.error("İstek atarken hata:", err);
        errorMsg.textContent = "Sunucuya bağlanırken bir hata oluştu.";
    }
});
