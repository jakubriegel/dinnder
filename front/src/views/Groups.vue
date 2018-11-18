<template>
    <div id="groups" class="groups container">
        <div class="row">
            <div class="col s12 m4">
                <ul class="collection z-depth-4" id="groups_list">
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
                <ul class="collection z-depth-4" id="events">
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
    import jquery from 'jquery'

    export default {
        data() {
            return {
                groups:[
                    { text: 'Group Error'}
                ],
                events:[
                    { text: 'Event Error'}
                ]
            }
        },
        methods: {
            sendQuery(name){
                console.log(name);
                axios
                    .get('http://10.254.50.28:8000/api/4/groups/' + name)
                    .then(response => (this.events = response.data.events))

                $(".active").removeClass("orange active")

            }
        },
        mounted () {
            axios
               .get('http://10.254.50.28:8000/api/4/groups')
                .then(response => (this.groups = response.data.groups))

            var e = document.getElementById("groups_list").firstChild;
            e.classList.add("orange");
            e.classList.add("active");

        }
    }
</script>

<style>
    .min-800 {
        min-height: 800px;
    }

</style>