$('.update-cart').on('click', function() {
    var productId = this.dataset.product
    var action = this.dataset.action
    $.ajax({
        url: '/update_item/',
        dataType: 'json',
        method:'POST',
        headers:{
            'X-CSRFToken':csrftoken,
        },
        data:JSON.stringify({'productId':productId, 'action':action}),
        success: function(data) {
        },
        error: e => {
            console.log(e.responseText);
        }
      });
});

$('.add-item').on('click', function() {
    var productId = this.dataset.product
    var action = this.dataset.action
    var orderId = this.dataset.order
    var element1 = document.getElementsByClassName("quantity-" + productId)
    var element2 = document.getElementsByClassName("get-total-" + productId)
    var element3 = document.getElementsByClassName("get-items-total-" + orderId)
    var element4 = document.getElementsByClassName("get-price-total-" + orderId)
    $.ajax({
        url: '/update_item/',
        dataType: 'json',
        method:'POST',
        headers:{
            'X-CSRFToken':csrftoken,
        },
        data:JSON.stringify({'productId':productId, 'action':action}),
        success: function(data) {
            element1[0].innerHTML = data["quantity"];
            element2[0].innerHTML = "$" + (data["get-total"].toFixed(2));
            element3[0].innerHTML = data["get-items-total"];
            element4[0].innerHTML = "$" + (data["get-price-total"].toFixed(2));
        },
        error: e => {
            console.log(e.responseText);
        }
      });
});

$('.subtract-item').on('click', function() {
    var productId = this.dataset.product
    var action = this.dataset.action
    var orderId = this.dataset.order
    var element1 = document.getElementsByClassName("quantity-" + productId)
    var element2 = document.getElementsByClassName("get-total-" + productId)
    var element3 = document.getElementsByClassName("get-items-total-" + orderId)
    var element4 = document.getElementsByClassName("get-price-total-" + orderId)
    if (element1[0].innerHTML == 1) {
        var deleteAction = confirm("Are you sure you want to delete this item?");
        if (deleteAction != false) {
            $.ajax({
                url: '/update_item/',
                dataType: 'json',
                method:'POST',
                headers:{
                    'X-CSRFToken':csrftoken,
                },
                data:JSON.stringify({'productId':productId, 'action':action}),
                success: function(data) {
                    $(".item-" + productId).remove();
                    element3[0].innerHTML = data["get-items-total"];
                    element4[0].innerHTML = "$" + (data["get-price-total"].toFixed(2));
                },
                error: e => {
                    console.log(e.responseText);
                }
              });
        }
    } else {
        $.ajax({
            url: '/update_item/',
            dataType: 'json',
            method:'POST',
            headers:{
                'X-CSRFToken':csrftoken,
            },
            data:JSON.stringify({'productId':productId, 'action':action}),
            success: function(data) {
                element1[0].innerHTML = data["quantity"];
                element2[0].innerHTML = "$" + (data["get-total"].toFixed(2));
                element3[0].innerHTML = data["get-items-total"];
                element4[0].innerHTML = "$" + (data["get-price-total"].toFixed(2));
            },
            error: e => {
                console.log(e.responseText);
            }
          });
    }
});

$('.remove-item').on('click', function() {
    var deleteAction = confirm("Are you sure you want to delete this item?");
    var productId = this.dataset.product
    var action = this.dataset.action
    var orderId = this.dataset.order
    var element3 = document.getElementsByClassName("get-items-total-" + orderId)
    var element4 = document.getElementsByClassName("get-price-total-" + orderId)
    if (deleteAction != false) {
        $.ajax({
            url: '/update_item/',
            dataType: 'json',
            method:'POST',
            headers:{
                'X-CSRFToken':csrftoken,
            },
            data:JSON.stringify({'productId':productId, 'action':action}),
            success: function(data) {
                $(".item-" + productId).remove();
                element3[0].innerHTML = data["get-items-total"];
                element4[0].innerHTML = "$" + (data["get-price-total"].toFixed(2));
            },
            error: e => {
                console.log(e.responseText);
            }
          });
    }
});