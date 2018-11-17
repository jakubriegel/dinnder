<template>
    <div id="groups" class="groups container">
        <div class="row">
            <div class="col s12">
                <div class="events">
                    <h4>This is an Events page {{groupId}}</h4>
                    <a href="#" @click.prevent="sendQuery(Id)">Try</a>
                </div>
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
                message: 'Guewno',
                groups:[
                    { text: 'Group ###'},
                    { text: 'Group ###'},
                    { text: 'Group ###'},
                    { text: 'Group ###'},
                    { text: 'Group ###'}
                ],
                Id: 21,
                info: null
            }
        },
        methods: {
            sendQuery(Id){
                console.log(this.info)
            }
        },
        mounted () {
            axios
                .get('https://api.coindesk.com/v1/bpi/currentprice.json')
                .then(response => (this.info = response))
        }
    }
</script>

