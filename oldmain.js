/*doc display*/
function openModal(image) {
            var modal = document.getElementById("myModal");
            var modalImg = document.getElementById("img01");
            modal.style.display = "block";
            modalImg.src = image.src;
        }

        function closeModal() {
            var modal = document.getElementById("myModal");
            modal.style.display = "none";
        }
/*End Doc display*/

/*Nav*/
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    document.querySelector(this.getAttribute('href')).scrollIntoView({
      behavior: 'smooth'
    });
  });
});
/*End Nav*/

/* somthings copilot said i should add*/

$(window).on('scroll', function () {
  if ($(window).scrollTop() + $(window).height() >= $(document).height()) {
  }
});

//copilot said i should add end 
