<template>
    <div id="groups" class="groups container">
        <div class="row">
            <div class="col s12 m4">
                <ul class="collection z-depth-4" id="groups_list">
                    <li class="collection-item avatar" v-for="group in groups" v-on:click="sendQuery(group.id)" :class="{orange:group.id == selected}" @click="selected = group.id">
                        <img v-bind:src="group.image" alt="photo" class="circle max-50">
                        <p>
                            <span class="title"><b>{{ group.name }}</b></span> <br>
                            {{group.description}}<br>
                        </p>
                    </li>
                </ul>
            </div>
            <div class="col s12 m8 min-800">
                <ul class="collection z-depth-4" id="events">
                    <li class="collection-item avatar animated fadeIn" v-for="event in events">
                        <img v-bind:src="event.image" alt="photo" class="circle max-50">
                        <p>
                            <span class="title"><b>{{ event.name }}</b></span>
                            <a class="btn-floating waves-effect waves-light orange right"><i class="material-icons">add</i></a>
                            <br>
                            {{event.description}}
                            <br>
                            <b>Place: </b><i>{{event.localizationName}}</i>
                            <br>
                            <span><b>Slots:</b> {{event.limitOfPeople}}</span>
                            <span class="right">{{event.dateOfEvent}}</span>
                        </p>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from "axios"
    import jquery from "jquery"

    if ($(window).width() < 601){
        $("#groups").toggle();
    }

    export default {
        data() {
            return {
                selected: undefined,
                groups:[
                    { text: 'Group Error'}
                ],
                events:[]
            }
        },
        methods: {
            sendQuery(id){
                axios
                    .get('http://10.254.50.28:8000/api/4/groups/' + id)
                    .then(response => (this.events = response.data.events))

                $(".active").removeClass("orange active");
                if ($(window).width() < 601){ window.location.replace("/events/" + id); }
            }
        },
        mounted () {
            axios
               .get('http://10.254.50.28:8000/api/4/groups')
                .then(response => (this.groups = response.data.groups));

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