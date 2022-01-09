let socket = io();
function runcode() {
    let code = document.getElementById("textbox").value;
    let sel = document.getElementById("vm-select").value;
    let mem = document.getElementById("memory-amount").valueAsNumber;
    console.log("function was called", code);
    socket.emit("run-code", code, sel, mem);
}
let textarea = document.getElementById("textbox");
let heightLimit = 1000; /* Maximum height: 200px */

textarea.oninput = function() {
  textarea.style.height = ""; /* Reset the height*/
  textarea.style.height = Math.min(textarea.scrollHeight, heightLimit) + "px";
};

socket.on("ksm-vm-output", (output) => {
    let convert = output.replace(/(?:\r\n|\r|\n)/g, "<br>");
    console.log(convert);
    document.getElementById("output").innerHTML = convert;
})

textarea.style.height = ""; /* Reset the height*/
textarea.style.height = Math.min(textarea.scrollHeight, heightLimit) + "px";