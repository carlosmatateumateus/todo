function look(action){
    let password = document.querySelector('#password')
    if (action == 'login'){
        if (password.type == 'password'){
            password.type = 'text'
        }
        else{
            password.type = 'password'
        }
    }
    else{
        let password_confirm = document.querySelector('#password-confirm')
        if (password.type == 'password' & password_confirm.type == 'password'){
            password.type = 'text'
            password_confirm.type = 'text'
        }
        else{
            password.type = 'password'
            password_confirm.type = 'password'
        }
    }
}
