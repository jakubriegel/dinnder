<template>
  <div id="app">
    <nav class="orange">
      <div id="nav" class="nav-wrapper left-align container">
        <!--<a href="#!" class="brand-logo">Dinnder</a>-->
        <img src="./assets/logo.png" alt="Logo" class="brand-logo logo-size">
        <a href="#" data-target="mobile-demo" class="sidenav-trigger"><i class="material-icons">menu</i></a>
        <ul class="right hide-on-med-and-down">
          <li><router-link to="/">Your groups</router-link></li>
          <li><router-link to="/myevents">My Events</router-link></li>
          <li><router-link to="/add_event">Add Event</router-link></li>
          <li><router-link to="/add_group">Add Group</router-link></li>
          <li><router-link to="/about">About</router-link></li>
        </ul>
      </div>
    </nav>

    <ul class="sidenav" id="mobile-demo">
      <li>
        <div class="user-view">
          <div class="background">
            <img src="./assets/office.jpg">
          </div>
          <a href="#user"><img class="circle" src="./assets/yuna.jpg"></a>
          <a href="#name"><span class="white-text name">John Doe</span></a>
          <a href="#email"><span class="white-text email">jdandturk@gmail.com</span></a>
      </div>
      </li>
      <li><router-link to="/">Your groups</router-link></li>
      <li><router-link to="/myevents">My Events</router-link></li>
      <li><router-link to="/add_event">Add Event</router-link></li>
      <li><router-link to="/add_group">Add Group</router-link></li>
      <li><router-link to="/about">About</router-link></li>
    </ul>
    <router-view/>
    <footer class="page-footer orange darken-1">
      <div class="container">
        <div class="row">
          <div class="col l9 s12">
            <h5 class="white-text">Czym jest Dinder?</h5>
            <p class="grey-text text-lighten-4">Znudzony jedzeniem samemu w swojej okolicy? Dinnder to aplikacja, dzięki której już nigdy nie spędzisz posiłku samotnie! Ponad 5000 zarejestrowanych restuaracji działających na terenie 12 największych miast w Polsce, a do tego co miesięczne promocje i kupony dla wszystkich aktywnych użytkówników. Poznawanie nowych ludzi jeszcze nigdy nie było tak proste! Skojrzystaj z ogromnej funkcjonalności, dzięki której będziesz mógł organizować eventy, tworzyć oraz dołączać do istniejących grup, a to wszystko za pomocą bardzo prostego i przejrzystego menu. Zaufało nam już ponad 50 tys. użytkowników, a z każdym miesiącem przybywa ich coraz więcej! Wypełnij 3 minutowy formularz i już dziś ciesz się życiem razem z Dinnderem.</p>
          </div>
          <div class="col l3 s12 right-align links hide-on-small-only">
            <h5 class="white-text">Łącza</h5>
            <ul>
              <li><router-link to="/">Your groups</router-link></li>
              <li><router-link to="/add_event">Add Event</router-link></li>
              <li><router-link to="/add_group">Add Group</router-link></li>
              <li><router-link to="/about">About</router-link></li>
            </ul>
          </div>
        </div>
      </div>
      <div class="footer-copyright">
        <div class="container">
          &copy; Forgotten Semicolon Development
        </div>
      </div>
    </footer>
    <button class="btn-large topButton waves-effect waves-light orange darken-1"><span class="material-icons">expand_less</span></button>

  </div>
</template>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>



