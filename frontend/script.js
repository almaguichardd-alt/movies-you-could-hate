// Load movies into the dropdown
fetch("http://127.0.0.1:5000/movies")
  .then(res => res.json())
  .then(movies => {
    const select = document.getElementById("movieSelect");
    movies.forEach(movie => {
      const option = document.createElement("option");
      option.value = movie.movie_id;
      option.textContent = movie.title;
      select.appendChild(option);
    });
  });

// Handle button click
document.getElementById("btn").addEventListener("click", () => {
  const movieId = document.getElementById("movieSelect").value;
  const loading = document.getElementById("loading");
  const results = document.getElementById("results");

  // Reset UI
  results.innerHTML = "";
  loading.style.display = "flex"; // show spinner

  // Show loading
  loading.style.display = "block";

  fetch(`http://127.0.0.1:5000/movies/${movieId}/hated`)
    .then(res => res.json())
    .then(data => {
      // Hide loading
      loading.style.display = "none";

      data.forEach(movie => {
        const div = document.createElement("div");
        div.className = "movie-card";

        div.innerHTML = `
          <img src="${movie.poster || 'https://placehold.co/200x300/444/FFF?text=Poster'}" class="poster">
          <p>${movie.title}</p>
        `;

        results.appendChild(div);
      });
    })
    .catch(err => {
      loading.style.display = "none";
      results.innerHTML = "<p>Error loading results.</p>";
    });
});


// Show loading state
results.innerHTML = "<div class='loading'>Loading...</div>";