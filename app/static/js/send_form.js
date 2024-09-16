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
                    
    if (response.status==200) {
        await render_message(message="Заявка успешно отправлена!")
    }
    else {
        await render_message(message="Упс! Что-то пошло не так...")
    }
}


async function render_message(message) {
    
    const app = Vue.createApp({});
        
    app.component('form-area', {
        template: `<form><h2 class="form_title">${message}</h2></form>`
    });
    app.mount('#app');
}