/* global bootstrap: false */
(() => {
  'use strict'
  const tooltipTriggerList = Array.from(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
  tooltipTriggerList.forEach(tooltipTriggerEl => {
    new bootstrap.Tooltip(tooltipTriggerEl)
  })
})()

/**
 * Easy selector helper function
 */
const select = (el, all = false) => {
  el = el.trim()
  if (all) {
    return [...document.querySelectorAll(el)]
  } else {
    return document.querySelector(el)
  }
}

/**
 * Easy event listener function
 */
const on = (type, el, listener, all = false) => {
  if (all) {
    select(el, all).forEach(e => e.addEventListener(type, listener))
  } else {
    select(el, all).addEventListener(type, listener)
  }
}

/**
 * Easy on scroll event listener 
 */
const onscroll = (el, listener) => {
  el.addEventListener('scroll', listener)
}

/**
 * Sidebar toggle
 */
if (select('.toggle-sidebar-btn')) {
  on('click', '.toggle-sidebar-btn', function(e) {
    select('body').classList.toggle('toggle-sidebar')
  })
}

  /**
   * Back to top button
   */
  let backtotop = select('.back-to-top')
  if (backtotop) {
  const toggleBacktotop = () => {
      if (window.scrollY > 100) {
      backtotop.classList.add('active')
      } else {
      backtotop.classList.remove('active')
      }
  }
  window.addEventListener('load', toggleBacktotop)
  onscroll(document, toggleBacktotop)
  }


window.onload = function () {
  function showSpinner(buttonId1, loadingId1, buttonId2, loadingId2) {
      document.getElementById(loadingId1).classList.remove("d-none");
      document.getElementById(buttonId1).setAttribute("disabled", "true");
      document.getElementById(loadingId2).classList.remove("d-none");
      document.getElementById(buttonId2).setAttribute("disabled", "true");

      // Add "d-none" class to the specified elements
      document.getElementById("form-local-pdf").classList.add("d-none");
      document.getElementById("modal-footer-local-pdf").classList.add("d-none");
      document.getElementById("form-linkedin-pdf").classList.add("d-none");
      document.getElementById("img-linkedin-pdf").classList.add("d-none");
      document.getElementById("modal-footer-linkedin").classList.add("d-none");
  }

  // Add an event listener to the form to trigger the spinner when submitted
  document.getElementById("cv-form").addEventListener("submit", function (event) {
      showSpinner("submit-button", "loading", "submit-button-2", "loading-2");
      // Optionally, you can prevent the form from submitting immediately
      // event.preventDefault();
  });
};