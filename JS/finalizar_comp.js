window.onload = function() {
    const total = localStorage.getItem('totalAmount'); 

    if (total !== null) {
        document.getElementById('totalInput').value = total; 
    }
}