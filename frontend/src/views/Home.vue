<template>
  <div class="home">
    <hr />
    <span class="is-size-3">Birthday list</span>
    <br />
    <br />
    <table class="table is-bordered is-narrow is-hoverable">
      <thead>
        <tr>
          <th>ID</th>
          <th>Navn</th>
          <th>Fødselsdato</th>
          <th>Alder</th>
          <th>Actions</th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="item in birthdayList" :key="item.id">
          <td>{{ item.id }}</td>
          <td>{{ item.name }}</td>
          <td>{{ item.birthDate }}</td>
          <td>{{ item.age }}</td>
          <td>
            <div class="buttons">
              <button class="button is-warning is-small">Endre</button>
              <button class="button is-danger is-small">Slett</button>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
  export default {
    name: 'Home',
    data() {
      return {
        birthdayList: [
          { id: 1, name: 'John', birthDate: '24.12.87', age: 33 },
          { id: 2, name: 'Arne', birthDate: '24.12.87', age: 44 },
          { id: 3, name: 'Bjarne', birthDate: '24.12.87', age: 12 },
          { id: 4, name: 'Bernt', birthDate: '24.12.87', age: 8 },
          { id: 5, name: 'Berit', birthDate: '24.12.87', age: 5 },
        ],
      }
    },
  }
</script>
