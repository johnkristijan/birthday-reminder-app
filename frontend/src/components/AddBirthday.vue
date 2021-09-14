<template>
  <form @submit="onSubmit" class="add-form">
    <div class="from-control">
      <label>Navn</label>
      <input type="text" name="name" v-model="name" placeholder="Legg til navn" />
    </div>

    <div class="from-control">
      <label>Fødselsdato</label>
      <date-picker v-model="birthDate" valueType="format"></date-picker>

      <div class="form-control form-control-check">
        <label>Ønsker du påminnelse på epost?</label>
        <input type="checkbox" v-model="reminder" name="reminder" />
      </div>

      <input type="submit" value="Legg til bursdag" class="btn btn-block" />
    </div>
  </form>
</template>

<script>
  import DatePicker from 'vue2-datepicker'
  import 'vue2-datepicker/index.css'

  export default {
    name: 'AddBirthday',
    components: { DatePicker },

    data() {
      return {
        name: '',
        birthDate: null,
        age: '',
        reminder: false,
        time1: null,
      }
    },

    methods: {
      onSubmit(e) {
        e.preventDefault() // <-hvorfor? fordi form submit er gammelt.

        if (!this.name) {
          alert('Du må legge til et navn til personen før du kan lagre.')
          return
        }
        const newBirthday = {
          name: this.name,
          birthDate: this.birthDate,
          age: this.age,
          reminder: this.reminder,
        }
        this.$emit('add-birthday', newBirthday)
        this.name = ''
        this.birthDate = ''
        this.age = ''
        this.reminder = false
      },
    },
  }
</script>

<style scoped>
  .add-form {
    margin-bottom: 40px;
  }

  .form-control {
    margin: 20px 0;
  }
  .form-control label {
    display: block;
  }
  .form-control input {
    width: 100%;
    height: 40px;
    margin: 5px;
    padding: 3px 7px;
    font-size: 17px;
  }
  .form-control-check {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .form-control-check label {
    flex: 1;
  }
  .form-control-check input {
    flex: 2;
    height: 20px;
  }
</style>
