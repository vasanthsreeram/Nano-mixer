var fieldHTML="<input type='text' class='form-control' id='Address-1' placeholder='XNO Address' value=''required=''><div class='invalid-feedback'>Valid XNO address is required.</div>"


var newAddCount = 0
function AddNewAddress() {
    newAddCount+=1
    document.getElementById("AddrField").innerHTML += fieldHTML
}