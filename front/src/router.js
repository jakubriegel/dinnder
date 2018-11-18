import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
        path: '/',
        name: 'groups',
        component: () => import('./views/Groups.vue')
    },
    {
        path: '/events',
        name: 'events',
        component: () => import('./views/Events.vue')
    },
    {
        path: '/add_event',
        name: 'add_event',
        component: () => import('./views/Add_event.vue')
    },
    {
        path: '/add_group',
        name: 'add_group',
        component: () => import( './views/Add_group.vue')
    },
    {
        path: '/about',
        name: 'about',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    },
    {
        path: '/events/:groupId',
        component: () => import('./views/Events.vue'),
        props: true,
    }
  ]
})
