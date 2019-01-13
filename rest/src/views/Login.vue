<template>
  <div>
    <NavHeader></NavHeader>
    <div>
      <table class="form-group">
        <tr>
          <th>Username:</th>
          <th><input type="text" class="form-control" v-model="username"></th>
        </tr>
        <br>
        <tr>
          <th>Password:</th>
          <th><input type="password" class="form-control" v-model="password"></th>
        </tr>
        <br>
        <tr>
          <th>Submit:</th>
          <th>
            <button class="btn btn-danger" @click="submit">submit</button>
          </th>
        </tr>
      </table>
    </div>
  </div>

</template>

<script>
import NavHeader from '@/components/NavHeader'

export default {
  name: 'Login',
  data () {
    return {
      username: '',
      password: ''
    }
  },
  components: { NavHeader },
  methods: {
    submit: function () {
      this.$axios.post('/api/login', { 'username': this.username, 'password': this.password })
        .then(response => {
          if (response.status === 200) {
            let expireDays = 60 * 60 * 24 * 7
            this.setCookie('token', response.data.token, expireDays)
            this.$router.go(-1)
          } else {
            alert('登录失败')
          }
        })
      // let token = 'Bearer ' + this.getCookie('token')
      // console.log(token)
      // this.$axios.get('http://127.0.0.1:5000/api/login_test', {headers: {'Authorization': token}})
      //   .then(response => {
      //     console.log(response.data)
      //   })
    }
  }
}
</script>

<style scoped>

</style>
