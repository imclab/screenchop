/*
 * login.js - Custom built js for the login process of Screenchop.
 *
 * Author: Alf
 *
 * Copyright (c) 2012 Screenchop
 * 
 * Licensed under the MIT license:
 *   http://www.opensource.org/licenses/mit-license.php
 *
 * Project home:
 *   http://www.github.com/alfg/screenchop
 */


// Dynamically clears username and password boxes when focus.
$(document).ready(function loginForm() {
 
	$('#pass-clear').show();
	$('#pass').hide();
 
	$('#pass-clear').focus(function() {
		$('#pass-clear').hide();
		$('#pass').show();
		$('#pass').focus();
	});
	$('#pass').blur(function() {
		if($('#pass').val() == '') {
			$('#pass-clear').show();
			$('#pass').hide();
		}
	});

	$('#user').each(function() {
		var default_value = this.value;
		$(this).focus(function() {
			if(this.value == default_value) {
				this.value = '';
			}
		});
		$(this).blur(function() {
			if(this.value == '') {
				this.value = default_value;
			}
		});
	});
	
	$('#pass-register-clear').show();
	$('#pass-register').hide();
 
	$('#pass-register-clear').focus(function() {
		$('#pass-register-clear').hide();
		$('#pass-register').show();
		$('#pass-register').focus();
	});
	$('#pass-register').blur(function() {
		if($('#pass-register').val() == '') {
			$('#pass-register-clear').show();
			$('#pass-register').hide();
		}
	});
	
    $('#pass-verify-clear').show();
	$('#pass-verify').hide();
 
	$('#pass-verify-clear').focus(function() {
		$('#pass-verify-clear').hide();
		$('#pass-verify').show();
		$('#pass-verify').focus();
	});
	$('#pass-verify').blur(function() {
		if($('#pass-verify').val() == '') {
			$('#pass-verify-clear').show();
			$('#pass-verify').hide();
		}
	});
	

	$('#user-register').each(function() {
		var default_value = this.value;
		$(this).focus(function() {
			if(this.value == default_value) {
				this.value = '';
			}
		});
		$(this).blur(function() {
			if(this.value == '') {
				this.value = default_value;
			}
		});
	});

// Checks if Username and/or Password are valid. If valid, redirect back to front page.
function submitLoginForm() {

var user = $("#user").val();
var pass = $("#pass").val();

$.ajax({
           type: "POST",
           url: "login",
           data: { username : user, password : pass }
            }).done(function( msg ) {
            
            if (msg == 'Success')
            {
            window.location.href = "/";
            }
            else {
            $('#login-message').html(msg);
            }
            });
            }

$("#submit").click(submitLoginForm);

function submitRegisterForm() {

var user = $("#user-register").val();
var pass = $("#pass-register").val();
var passVerify = $("#pass-verify").val();

$.ajax({
           type: "POST",
           url: "register",
           data: { username : user, password : pass, verify : passVerify }
            }).done(function( msg ) {
            
            if (msg == 'Success')
            {
            window.location.href = "/";
            }
            else {
            $('#register-message').html(msg);
            }
            });
            }

$("#submit2").click(submitRegisterForm);


// End (document).ready()
});
