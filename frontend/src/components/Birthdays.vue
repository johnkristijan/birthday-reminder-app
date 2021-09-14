<template>
  <div>
    <div :key="birthday.id" v-for="birthday in birthdays">
      <Birthday
        @toggle-reminder="$emit('toggle-reminder', birthday.id)"
        @delete-birthday="$emit('delete-birthday', birthday.id)"
        :birthday="birthday"
      />
    </div>
  </div>
</template>

<script>
  import Birthday from './Birthday'
  export default {
    name: 'Birthdays',
    props: {
      birthdays: Array,
    },
    components: {
      Birthday,
    },
    emits: ['toggle-reminder', 'delete-birthday'],
  }
</script>
