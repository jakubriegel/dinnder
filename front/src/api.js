import Vue from 'vue'
import axios from 'axios'

const client = axios.create({
    baseURL: 'http://localhost:8080/',
    json: true
})

export default {
    getPosts (id) {
       console.log('ask')
    },
    getPost (id) {
        return this.execute('get', `/posts/${id}`)
    },
    createPost (data) {
        return this.execute('post', '/posts', data)
    },
    updatePost (id, data) {
        return this.execute('put', `/posts/${id}`, data)
    },
    deletePost (id) {
        return this.execute('delete', `/posts/${id}`)
    }
}