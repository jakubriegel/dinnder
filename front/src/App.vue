<template>
  <div id="app">
    <nav class="orange">
      <div id="nav" class="nav-wrapper left-align container">
        <a href="#!" class="brand-logo">Dinnder</a>
        <a href="#" data-target="mobile-demo" class="sidenav-trigger"><i class="material-icons">menu</i></a>
        <ul class="right hide-on-med-and-down">
          <li><router-link to="/">Home</router-link></li>
          <li><router-link to="/groups">Your groups</router-link></li>
          <li><router-link to="/events">Events</router-link></li>
          <li><router-link to="/add_event">Add Event</router-link></li>
          <li><router-link to="/add_group">Add Group</router-link></li>
          <li><router-link to="/about">About</router-link></li>
        </ul>
      </div>
    </nav>

    <ul class="sidenav" id="mobile-demo">
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/groups">Your groups</router-link></li>
      <li><router-link to="/events">Events</router-link></li>
      <li><router-link to="/add_event">Add Event</router-link></li>
      <li><router-link to="/add_group">Add Group</router-link></li>
      <li><router-link to="/about">About</router-link></li>
    </ul>
    </ul>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>



