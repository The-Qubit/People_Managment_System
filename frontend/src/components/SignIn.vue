<template>
    <h1>
        Login
    </h1>
    <div class="register">
        <input type="text" v-model="name" placeholder="Enter Email" />
        <input type="password" v-model="name" placeholder="Enter password" />
        <p>
            <button v-on:click="signUp">Login</button>
        </p>
    </div>
</template>

<script>
  export default { name: 'SignIn' }
</script>


<style scoped>
.logo {
  width: 100px;
}

.register input {
  width: 300px;
  height: 30px;
  padding-left: 20px;
  display: block;
  margin-bottom: 30px;
  margin-right: auto;
  margin-left: auto;
  border: 1px solid skyblue;
}

.register button {
  width: 320px;
  height: 40px;
  border: 1px solid skyblue;
  background: skyblue;
  color: #fff;
  cursor: pointer;
} 
</style>
