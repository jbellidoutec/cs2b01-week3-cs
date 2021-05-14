function calculate(){
    element_soles = document.getElementById("monto");
    element_usd = document.getElementById("monto_usd");
    element_usd.value = element_soles.value / 3.86;
}