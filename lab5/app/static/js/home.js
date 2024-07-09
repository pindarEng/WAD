document.addEventListener('DOMContentLoaded', function() {
    const addProductForm = document.getElementById("addProductForm");
    const deleteProductForm = document.getElementById("deleteProductForm");
    const modifyProductForm = document.getElementById("modifyProductForm");

    function getCSRFToken() {
        const csrfToken = document.cookie.split(';').find(cookie => cookie.trim().startsWith('csrftoken='));
        return csrfToken ? csrfToken.split('=')[1] : null;
    }

    addProductForm.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const formData = new FormData(addProductForm);
        const product = {
            name: formData.get('name'),
            type: formData.get('type'),
            description: formData.get('description'),
            price: formData.get('price')
        };

        fetch('/products/addProduct/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken()
            },
            body: JSON.stringify(product)
        })
        .then(response => {
            if (response.ok) {
                refreshProducts();
                addProductForm.reset();
            } else {
                console.error('Error adding product:', response.status);
            }
        });
    });

    deleteProductForm.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const productId = deleteProductForm.querySelector('#deleteProductId').value;

        fetch(`/products/${productId}/delete/`, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': getCSRFToken()
            }
        })
        .then(response => {
            if (response.ok) {
                refreshProducts();
                deleteProductForm.reset();
            } else {
                console.error('Error deleting product:', response.status);
            }
        });
    });

    modifyProductForm.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const formData = new FormData(modifyProductForm);
        const product = {
            name: formData.get('name'),
            price: formData.get('price')
        };
        const productId = formData.get('id');

        fetch(`/products/${productId}/modify/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken()
            },
            body: JSON.stringify(product)
        })
        .then(response => {
            if (response.ok) {
                refreshProducts();
                modifyProductForm.reset();
            } else {
                console.error('Error modifying product:', response.status);
            }
        });
    });

    function refreshProducts() {
        fetch('/products/')
        .then(response => response.json())
        .then(data => showProducts(data));
    }

    function showProducts(products) {
        const prodDiv = document.getElementById("products");
        const deleteProductIdSelect = document.getElementById("deleteProductId");
        const modifyProductIdSelect = document.getElementById("modifyProductId");

        prodDiv.innerHTML = "";
        deleteProductIdSelect.innerHTML = "";
        modifyProductIdSelect.innerHTML = "";

        products.forEach(product => {
            let addedProd = document.createElement("div");
            addedProd.innerHTML = `${product.id} ${product.name} ${product.price}`;
            prodDiv.appendChild(addedProd);

            let deleteOption = document.createElement("option");
            deleteOption.value = product.id;
            deleteOption.text = product.id;
            deleteProductIdSelect.appendChild(deleteOption);

            let modifyOption = document.createElement("option");
            modifyOption.value = product.id;
            modifyOption.text = product.id;
            modifyProductIdSelect.appendChild(modifyOption);
        });
    }

    refreshProducts();
});
