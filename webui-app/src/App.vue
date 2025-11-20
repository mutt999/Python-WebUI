<template>
  <div id="app" class="ui segment" style="margin: 5px;">
    <p class="ui segment">{{ info }}</p>
    <p class="ui segment">{{ month }}</p>
    <div class="ui input">
      <input v-model="eventName" @keyup.enter="addEvent" placeholder="Neue Veranstaltung" />
      <div class="ui primary button" @click="addEvent">Hinzufügen</div>
    </div>
    <div class="ui divider"></div>
    <div class="ui cards">
      <event-item v-for="(event, index) in events" :key="event.id" :event="event" :index="index"
        @remove-event="removeEvent(event)" @update-event="updateEvent(event)" />
    </div>
  </div>
</template>

<script setup lang="ts">

import { ref, inject, onMounted } from 'vue'
import EventItem from './components/EventItem.vue'
import type { IEvent, IEvents, IEventService } from './eventservice.ts'

const eventService = inject('IEventService') as IEventService
const month = ref('Januar')
const eventName = ref('')
const info = ref('Vue-Instanz...')
const events = ref<IEvents>([])

onMounted(
  async () => { events.value = await eventService.GetEvents(month.value); }
);

const addEvent = async () => {
  events.value = await eventService.AddEvent(eventName.value, 0)
  eventName.value = ''
}

const removeEvent = async (event: IEvent) => {
  events.value = await eventService.RemoveEvent(event.id)
}

const updateEvent = async (event: IEvent) => {
  events.value = await eventService.UpdateEvent(event)
}

</script>

