<template>
  <div @dblclick="$emit('toggle-reminder', birthday.id)" v-bind:class="[birthday.reminder ? 'reminder' : '', 'birthday']">
    <h3>
      {{ birthday.name }} er {{ age }} gammel, og er født i
      {{ birthday.birthDate }}
      <i @click="clickHandler()" class="fas fa-edit"> </i>
      <i @click="$emit('delete-birthday', birthday.id)" class="fas fa-times"></i>
    </h3>
  </div>
</template>

<script>
  import moment from 'moment'

  export default {
    name: 'Birthday',
    props: {
      birthday: Object,
    },
    computed: {
      age() {
        const diffTime = moment(this.birthday.birthDate).fromNow(true)
        return diffTime
      },
    },
    created() {
      moment.locale('nb')
    },
  }
</script>

<style scoped>
  .h3 {
    display: inline;
  }
  i.fas.fa-times::before {
    color: red;
  }
  i.fas.fa-edit::before {
    color: rgb(0, 0, 0);
  }
  input {
    background: #f4f4f4;
    margin: 5px;
    padding: 10px 20px;
    cursor: pointer;
  }

  .birthday {
    background: #f4f4f4;
    margin: 5px;
    padding: 10px 20px;
    cursor: pointer;
  }
  .birthday.reminder {
    border-left: 5px solid green;
  }
  .birthday h3 {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 5px;
  }
  .birthday i {
    justify-content: right;
  }
</style>
