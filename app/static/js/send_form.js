async function send_form() {
    // получаем введеные данные
    const username = document.getElementById("username").value;
    const phonenumber = document.getElementById("phonenumber").value;
    const email = document.getElementById("email").value;

    // отправляем запрос
    const response = await fetch("/form", {
                    method: "POST",
                    headers: { "Accept": "application/json", 
                      "Content-Type": "application/json" },
                    body: JSON.stringify({ 
                        username: username,
                        phonenumber: phonenumber,
                        email: email
                        })
                    });
    if (response.ok) {
        // Если получилось, то выводим сообщение об успешном отправлении
    }
    else {
        // Если не получилось, то выводим сообщение об ошибке
    }
}