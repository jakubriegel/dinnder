<template>
  <div id="app">
    <nav class="orange">
      <div id="nav" class="nav-wrapper left-align container">
        <a href="#!" class="brand-logo">Dinnder</a>
        <a href="#" data-target="mobile-demo" class="sidenav-trigger"><i class="material-icons">menu</i></a>
        <ul class="right hide-on-med-and-down">
          <li><router-link to="/">Home</router-link></li>
          <li><router-link to="/groups">Your groups</router-link></li>
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
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/groups">Your groups</router-link></li>
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
            <p class="grey-text text-lighten-4">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vel urna ut risus accumsan auctor. Pellentesque quis porta dolor. Suspendisse in mauris convallis, varius orci eget, lacinia quam. Nulla convallis consectetur urna id tempus. Nullam cursus euismod accumsan. Mauris feugiat at urna tincidunt eleifend. Sed risus magna, dapibus eu molestie nec, rhoncus ac urna. Aenean fermentum, velit at laoreet laoreet, odio dolor volutpat ex, vel tempor orci quam vel dui.</p>
          </div>
          <div class="col l3 s12 right-align links hide-on-small-only">
            <h5 class="white-text">Łącza</h5>
            <ul>
              <li><router-link to="/">Home</router-link></li>
              <li><router-link to="/groups">Your groups</router-link></li>
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



