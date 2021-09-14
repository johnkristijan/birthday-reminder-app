<template>
  <div class="container">
    <NavBar />

    <span class="is-size-3">Birthday list</span>
    <Button @btn-click="toggleAddBirthday" :btnText="showAddBirthday ? 'Avbryt' : 'Legg til en fødselsdag'" />
    <div v-if="showAddBirthday">
      <AddBirthday @add-birthday="addBirthday" />
    </div>
    <Birthdays @toggle-reminder="toggleReminder" @delete-birtdhay="deleteBirthday" :birthdays="birthdays" />
  </div>
</template>

<script>
  import NavBar from '../components/NavBar'
  import Button from '../components/Button'
  import AddBirthday from '../components/AddBirthday'
  import Birthdays from '../components/Birthdays'

  export default {
    name: 'Home',
    components: {
      Button,
      Birthdays,
    },
    data() {
      return {
        birthdays: [],
        showAddBirthday: false,
      }
    },
    components: {
      NavBar,
      Button,
      AddBirthday,
      Birthdays,
    },
    methods: {
      toggleAddBirthday() {
        this.showAddBirthday = !this.showAddBirthday
      },

      async toggleReminder(id) {
        const birthdayToToggle = await this.fetchBirthday(id)

        const updBirthday = {
          ...birthdayToToggle,
          reminder: !birthdayToToggle.reminder,
        }

        const response = await fetch(`http://localhost:5001/birthdays/${id}`, {
          method: 'PUT',
          headers: {
            'Content-type': 'application/json',
          },
          body: JSON.stringify(updBirthday),
        })

        const data = await response.json()

        this.birthdays = this.birthdays.map(birthday => (birthday.id === id ? { ...birthday, reminder: data.reminder } : birthday))
      },
      async deleteBirthday(id) {
        if (confirm('Are you sure?')) {
          const response = await fetch(`http://localhost:5001/birthdays/${id}`, {
            method: 'DELETE',
          })
          response.status === 200
            ? (this.birthdays = this.birthdays.filter(birthday => birthday.id !== id))
            : alert('Error deleting birthday.')
        }
      },

      async addBirthday(birthday) {
        try {
          const response = await fetch('http://localhost:5001/birthdays', {
            method: 'POST',
            headers: {
              'Content-type': 'application/json',
            },
            body: JSON.stringify(birthday),
          })

          const data = await response.json()
          this.birthdays = [...this.birthdays, data]
          console.log('Added birthday!')
          console.log(data)
        } catch (err) {
          console.log(err)
        }
      },
      async fetchBirthdays() {
        const resonse = await fetch('http://localhost:5001/birthdays')
        const data = await resonse.json()
        return data
      },
      async fetchBirthday(id) {
        const resonse = await fetch(`http://localhost:5001/birthdays/${id}`)
        const data = await resonse.json()
        return data
      },
    },
    async created() {
      this.birthdays = await this.fetchBirthdays()
    },
  }
</script>

<style>
  .container {
    max-width: 90%;
    margin: 30px auto;
    overflow: auto;
    min-height: 300px;
    padding: 30px;
    border-radius: 5px;
  }
</style>
