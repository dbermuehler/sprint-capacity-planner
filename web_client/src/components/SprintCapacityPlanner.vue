<template>
  <h1 v-if="currentSprint">Sprint: {{ currentSprint.name }}</h1>
  <table v-if="currentSprint" class="table">
      <thead>
      <tr>
          <th>Team Member</th>
          <th>Participation in Sprint</th>

          <th>Wednesday</th>
          <th>Thursday</th>
          <th>Friday</th>
          <th>Monday</th>
          <th>Tuesday</th>
          <th>Wednesday</th>
          <th>Thursday</th>
          <th>Friday</th>
          <th>Monday</th>
          <th>Tuesday</th>

          <th>Workhours in Sprint</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="member, name in currentSprint.capacities" :key="name">
          <th>{{ name }}</th>
          <td><input type="text" name="number" min="1" max="100" v-model="member.participation"></td>
          <td v-for="availableWorkHours in member.sprintDays" :key="availableWorkHours">
            <input type="number" min="1" max="8" :value="availableWorkHours">
          </td>
          <td>{{ totalWorkHoursOf(member) }}</td>
      </tr>
      </tbody>

      <div>
          <tbody>
          <tr>
              <th>Team Capacity (in hours)</th>
              <td>{{ teamCapacityTotalHours }}</td>
          </tr>
          <tr>
              <th>Weeks</th>
              <td>{{ teamCapacityWeeks }}</td>
          </tr>
          <tr>
              <th>Days</th>
              <td>{{ teamCapacityDays }}</td>
          </tr>
          <tr>
              <th>Hours</th>
              <td>{{ teamCapacityHours }}</td>
          </tr>
          </tbody>
      </div>
  </table>
</template>

<script>
import  axios from 'axios'

export default {
  name: 'SprintCapacityPlanner',
  data () {
    return {
      currentSprint: null
    }
  },
  computed: {
    teamCapacityTotalHours: function() {
      return Object.values(this.currentSprint.capacities)
              .map(member => this.totalWorkHoursOf(member))
              .reduce((a,b) => a+b)
    },
    teamCapacityWeeks: function() {
      return Math.floor((this.teamCapacityTotalHours / 8) / 5)
    },
    teamCapacityDays: function() {
      return Math.floor((this.teamCapacityTotalHours - this.teamCapacityWeeks*5*8) / 8)
    },
    teamCapacityHours: function() {
      return Math.floor(this.teamCapacityTotalHours - (this.teamCapacityWeeks*5*8 + this.teamCapacityDays*8))
    },
  },
  methods: {
    totalWorkHoursOf: (member) => member.sprintDays.reduce((a,b) => a+b) * member.participation
  },
  mounted () {
    axios.get('http://127.0.0.1:5000/sprints').then(response => {
      const firstSprint = Object.keys(response.data)[0]
      this.currentSprint = response.data[firstSprint]
    })
  }
}
</script>

<style scoped></style>
