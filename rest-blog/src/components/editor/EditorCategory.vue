<template>
  <div>
    <table class="form-group">
      <tr>
        <th>Category:</th>
        <th><input type="text" class="form-control" v-model="name"></th>
      </tr>
      <br>
      <br>
      <tr>
        <th>提交</th>
        <th>
          <button class="btn btn-danger" @click="submit">submit</button>
        </th>
      </tr>
    </table>
    <br>

  </div>
</template>

<script>
  export default {
    name: "EditorCategory",
    data() {
      return {
        name: '',
        category_id: '',
      }
    },
    mounted() {
      this.name = this.$route.params.name;
      this.$axios.get('http://127.0.0.1:5000/api/category_operation', {params: {'name': this.name}}, {headers: {'Authorization': 'Bearer '+ this.getCookie('token')}})
        .then(response => {
          this.category_id = response.data.category.id;
        })
    },
    methods: {
      submit: function () {
        this.$axios.put('http://127.0.0.1:5000/api/category_operation', {'id': this.category_id, 'name': this.name}, {headers: {'Authorization': 'Bearer '+ this.getCookie('token')}})
          .then(response => {
            if (response.status === 200) {
              alert('修改成功')
            }
          })
      }
    },
  }
</script>

<style scoped>

</style>
