document.addEventListener('DOMContentLoaded', function() {
    const addProductForm = document.getElementById("addProductForm");
    const deleteProductForm = document.getElementById("deleteProductForm");
    const modifyProductForm = document.getElementById("modifyProductForm");

    // Function to fetch CSRF token from cookies
    function getCSRFToken() {
        const csrfToken = document.cookie.split(';').find(cookie => cookie.trim().startsWith('csrftoken='));
        return csrfToken ? csrfToken.split('=')[1] : null;
    }

    // Add product button click event
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

    // Delete product button click event
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

    // Modify product button click event
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

    // Function to refresh products list
    function refreshProducts() {
        fetch('/products/')
        .then(response => response.json())
        .then(data => showProducts(data));
    }

   // Function to display products
    function showProducts(products) {
        const prodDiv = document.getElementById("products");
        const deleteProductIdSelect = document.getElementById("deleteProductId");
        const modifyProductIdSelect = document.getElementById("modifyProductId");

        prodDiv.innerHTML = "";
        deleteProductIdSelect.innerHTML = "";
        modifyProductIdSelect.innerHTML = "";

        products.forEach(product => {
            // Display product in product list
            let addedProd = document.createElement("div");
            addedProd.innerHTML = `${product.id} ${product.name} ${product.price}`;
            prodDiv.appendChild(addedProd);

            // Add option to delete product select
            let deleteOption = document.createElement("option");
            deleteOption.value = product.id;
            deleteOption.text = product.id;
            deleteProductIdSelect.appendChild(deleteOption);

            // Add option to modify product select
            let modifyOption = document.createElement("option");
            modifyOption.value = product.id;
            modifyOption.text = product.id;
            modifyProductIdSelect.appendChild(modifyOption);
        });
    }

    // Initial load of products
    refreshProducts();
});
