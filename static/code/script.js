const body = document.getElementById('body');
const theme = document.getElementById('theme');

console.log('Hello!')

theme.addEventListener('click', ()=>{
    console.log('ok')
    if (body.style.background == 'black'){
        body.style.backgroundColor = 'white'
    }else{
        body.style.backgroundColor = 'black'
    }
});

