// var button = document.querySelectorAll(".recently")[0];
// for all in button;
//     button.addEventListener('click', function() {
//       if (button.getAttribute("data-text-swap",) == button.innerHTML) {
//         button.innerHTML = button.getAttribute("data-text-original");
//       } else {
//         button.setAttribute("data-text-original", button.innerHTML);
//         button.innerHTML = button.getAttribute("data-text-swap");
//       }
//     }, false);
//

document.querySelector('button').addEventListener('click', function () {
    document.querySelector('.churn-date').classList.toggle('hidden');
});