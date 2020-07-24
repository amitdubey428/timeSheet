type = ['primary', 'info', 'success', 'warning', 'danger'];
noti = {
	popNotification: function(from, align) {
	        color = Math.floor((Math.random() * 4) + 1);

	        $.notify({
	            icon: "nc-icon nc-app",
	            message: "Welcome to timeSheet - hope you are on schedule."

	        }, {
	            type: type[color],
	            timer: 8000,
	            placement: {
	                from: from,
	                align: align
	            }
	        });
	    }
}