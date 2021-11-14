<template>
  <sprint-capacity-planner/>
</template>

<script>
import SprintCapacityPlanner from './components/SprintCapacityPlanner.vue'

export default {
  name: 'App',
  components: {
    SprintCapacityPlanner
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
