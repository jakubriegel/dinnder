<template>
    <div id="groups" class="groups container">
        <div class="row">
            <div class="col s12">
                <div class="add_group">
                    <form id="add_group" name="add_group" v-on:submit.prevent="submitForm">
                        <h4>Add Event</h4>
                        <div class="input-field col s12">
                            <input id="group_name" v-model="groupname" name="group_name" type="text" class="">
                            <label for="group_name">Group Name</label>
                        </div>
                        <div class="input-field col s12">
                            <input id="group_image" v-model="image" type="text" class="">
                            <label for="group_image">Image URL</label>
                        </div>
                        <div class="input-field col s12">
                            <input id="group_desc" v-model="description" type="text" class="">
                            <label for="group_desc">Description</label>
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
    import jquery from "jquery"
    export default {
        data() {
            return {
                userid:"4",
                groupname: undefined,
                image: undefined,
                description: undefined
            }
        },
        methods:{
            submitForm(){

                console.log(this.group_name);
                // axios.post('http://10.254.50.28:8000/api/4/create/group',
                //     {
                //      "userid":"4",
                //      "groupname":this.group_name
                //     }, // the data to post
                //     { headers: {
                //             'Content-type': 'application/x-www-form-urlencoded',
                //         }
                //     });
                M.toast({html: 'Event added!', classes: 'rounded'});
            }
        },
        mounted(){
        }
    }
</script>