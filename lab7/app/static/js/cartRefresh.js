document.addEventListener('DOMContentLoaded', function() {
    function updateTotalPrice() {
        let totalPrice = 0;
        const cartItems = document.querySelectorAll('#cart-items li');
        cartItems.forEach(function(item) {
            const price = parseFloat(item.querySelector('.productPrice').dataset.price);
            const quantity = parseInt(item.querySelector('.quantityInput').value);
            totalPrice += price * quantity;
        });
        document.getElementById('totalPrice').textContent = totalPrice.toFixed(2);
    }

    // Add event listeners to all quantity input fields
    const quantityInputs = document.querySelectorAll('.quantityInput');
    quantityInputs.forEach(function(input) {
        input.addEventListener('input', function() {
            updateTotalPrice();
        });
    });

    updateTotalPrice();
});