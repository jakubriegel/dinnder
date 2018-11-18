<template>
    <div id="groups" class="groups container">
        <div class="row">
            <div class="col s12 m8 min-800">
                <ul class="collection z-depth-4" id="events">
                    <li class="collection-item avatar animated fadeIn" v-for="event in events">
                        <img v-bind:src="event.image" alt="photo" class="circle max-50">
                        <p>
                            <span class="title"><b>{{ event.name }}</b></span>
                            <a class="btn-floating waves-effect waves-light orange right"><i class="material-icons" v-on:click="singup(event.id, event.group.id)">add</i></a>
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
    import axios from 'axios'
    
    export default {
        props: ['groupId'],
        data() {
            return {
                selected: undefined,
                events:[]
            }
        },
        methods: {
            sendQuery(id){
                if(id == 0) {
                    axios
                        .get('http://10.254.50.28:8000/api/4/nearby/52.399455396/16.930157362')
                        .then(response => (this.events = response.data.events))
                }
                else {
                    axios
                        .get('http://10.254.50.28:8000/api/4/groups/' + id)
                        .then(response => (this.events = response.data.events));
                }
            },
            singup(eventId, groupId) {
                axios
                    .post('http://10.254.50.28:8000/api/4/' + groupId + '/' + eventId + '/takepartin')
            }
        },
        mounted() {
            this.sendQuery(this.groupId);
        }
    }

</script>

