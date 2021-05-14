function saludar(){
    alert("hola")
}

function calculate(){
    txt_soles = document.getElementById("txt_soles")
    mnt_soles = txt_soles.value
    console.log(mnt_soles)
    txt_dolares = document.getElementById("txt_dolares")
    mnt_dolares = mnt_soles/3.83
    txt_dolares.value = mnt_dolares
    console.log(txt_dolares)
    console.log($('#txt_soles'))
}