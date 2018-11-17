<template>
    <div id="groups" class="groups container">
        <div class="row">
            <div class="col s12 m4">
                <ul class="collection z-depth-4">
                    <li class="collection-item avatar" v-for="group in groups" v-on:click="sendQuery(group.name)">
                        <img src="../assets/yuna.jpg" alt="photo" class="circle max-50">
                        <p>
                            <span class="title">{{ group.name }}</span> <br>
                            {{group.id}}
                        </p>
                    </li>
                </ul>
            </div>
            <div class="col s12 m8 min-800">
                <ul class="collection z-depth-4 ">
                    <li class="collection-item avatar" v-for="event in events">
                        <img src="../assets/yuna.jpg" alt="photo" class="circle max-50">
                        <p>
                            <span class="title">{{ event.name }}</span> <br>
                            {{event.localization}}
                        </p>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from "axios"

    export default {
        data() {
            return {
                groups:[
                    { text: 'Group ###'},
                    { text: 'Group ###'},
                    { text: 'Group ###'},
                    { text: 'Group ###'},
                    { text: 'Group ###'}
                ],
                events:[
                    { text: 'Event 123'},
                    { text: 'Event 123'},
                    { text: 'Event 123'},
                    { text: 'Event 123'},
                    { text: 'Event 123'},
                    { text: 'Event 123'},
                    { text: 'Event 123'},
                    { text: 'Event 123'},
                    { text: 'Event 123'},
                    { text: 'Event 123'},
                    { text: 'Event 123'},
                ],
                groups_test: null
            }
        },
        methods: {
            sendQuery(name){
                console.log(this.groups_test);
                console.log(name);
                axios
                    .get('http://10.254.50.28:8000/api/4/groups/' + name)
                    .then(response => (this.events = response.data.events))
            }
        },
        mounted () {
            axios
               .get('http://10.254.50.28:8000/api/4/groups')
                .then(response => (this.groups = response.data.groups))
                 //.then(this.groups = this.group_test.groups)
            //if(this.groups_test.groups) this.groups = this.groups_test
        }
    }
</script>

<style>
    .min-800 {
        min-height: 800px;
    }

</style>