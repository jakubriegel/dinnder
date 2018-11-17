<template>
    <div id="groups" class="groups container">
        <div class="row">
            <div class="col s12 m4">
                <ul class="collection z-depth-4">
                    <li class="collection-item avatar" v-for="group in groups">
                        <img src="../assets/yuna.jpg" alt="photo" class="circle max-50">
                        <p>
                            <span class="title">{{ group.text }}</span> <br>
                            {{group.text}}
                        </p>
                    </li>
                </ul>
            </div>
            <div class="col s12 m8 min-800">
                <ul class="collection z-depth-4 ">
                    <li class="collection-item avatar" v-for="event in events">
                        <img src="../assets/yuna.jpg" alt="photo" class="circle max-50">
                        <p>
                            <span class="title">{{ event.text }}</span> <br>
                            {{event.text}}
                        </p>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
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
            }
        }
    }
</script>

<style>
    .min-800 {
        min-height: 800px;
    }

</style>