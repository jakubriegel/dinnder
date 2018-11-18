<template>
    <div id="groups" class="groups container">
        <div class="row">
            <div class="col s12">
                <div class="add_event">
                    <form id="add_event" name="add_group" v-on:submit.prevent="submitForm">
                        <h4>Add Event</h4>
                        <div class="input-field col s12">
                            <input id="eventname" v-model="eventname" type="text" class="">
                            <label for="eventname">Event name</label>
                        </div>
                        <div class="input-field col s12">
                            <select class="icons" v-model="groupid">
                                <option value="" disabled selected>Choose your option</option>
                                <option v-for="group in groups" v-bind:value="group.id" v-bind:data-icon="group.image">{{group.name}}</option>
                            </select>
                            <label>Images in select</label>
                        </div>
                        <div class="input-field col s12">
                            <input id="image" v-model="image" type="text" class="">
                            <label for="image">Image URL</label>
                        </div>
                        <div class="input-field col s12">
                            <input id="localizationName" v-model="localizationName" type="text" class="">
                            <label for="localizationName">Localization name </label>
                        </div>
                        <!--<div class="input-field col s12">-->
                            <!--<input id="localizationLNG" v-model="localizationLNG" type="text" class="">-->
                            <!--<label for="localizationLNG">LNG</label>-->
                        <!--</div>-->
                        <!--<div class="input-field col s12">-->
                            <!--<input id="localizationLAT" v-model="localizationLAT" type="text" class="">-->
                            <!--<label for="localizationLAT">LAT</label>-->
                        <!--</div>-->
                        <div class="input-field col s12">
                            <input id="description" v-model="description" type="text" class="">
                            <label for="description">Description</label>
                        </div>
                        <div class="input-field col s12">
                            <input id="dateOfEvent" v-model="dateOfEvent" type="text" class="">
                            <label for="dateOfEvent">Date of event</label>
                        </div>
                        <div class="input-field col s12">
                            <input id="limitOfPeople" v-model="limitOfPeople" type="text" class="">
                            <label for="limitOfPeople">Slots</label>
                        </div>
                        <div class="col s12 margin12">
                            <button class="btn waves-effect waves-light orange" id="submit" type="submit" name="action">Submit
                                <i class="material-icons right">send</i>
                            </button>
                        </div>
                        <div class="col s12 margin12">
                            <button class="btn waves-effect waves-light orange" id="reset" type="reset" name="action">reset
                                <i class="material-icons right">send</i>
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from "axios"
    import jquery from "jquery"
    export default {
        data() {
            return {
                groups:[
                    { text: 'Group Error'}
                ],
                userid:"4",
                groupid: undefined,
                eventname: undefined,
                image: undefined,
                localizationName: undefined,
                localizationLNG: 16.925168,
                localizationLAT: 52.406374,
                description: undefined,
                dateOfEvent: undefined,
                limitOfPeople: undefined
            }
        },
        methods:{
            submitForm(){
                axios.post("http://10.254.50.28:8000/api/4/"+ this.groupid +"/create/event",
                    {
                        "userid":this.userid,
                        "groupid":this.groupid,
                        "eventname":this.eventname,
                        "image":this.image,
                        "localizationName":this.localizationName,
                        "localizationLNG":this.localizationLNG,
                        "localizationLAT":this.localizationLAT,
                        "description":this.description,
                        "dateOfEvent":this.dateOfEvent,
                        "limitOfPeople":this.limitOfPeople
                    }, // the data to post
                    { headers: {
                            'Content-type': 'application/x-www-form-urlencoded',
                        }
                    });
                M.toast({html: 'Event added!', classes: 'rounded'});
            },
            updateSelect(){
                window.onload = function () {
                    $('select').formSelect();
                }
            }
        },
        mounted(){
            axios
                .get('http://10.254.50.28:8000/api/4/groups')
                .then(response => (this.groups = response.data.groups));
                setTimeout(this.updateSelect(), 1000);

        }
    }
</script>