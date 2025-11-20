<template>
  <div class="card">
    <div class="content">
      <remove-button class="ui right floated" @remove="emit('removeEvent', event)" />
      <a class="header">{{ event.name }}</a>
      <div class="meta">
        <span class="date">{{ index + 1 }}:{{ event.id }}</span>
      </div>
    </div>
    <div class="extra content" @click.left="event.participantCount++; emit('updateEvent', event)"
      @click.right="event.participantCount--; emit('updateEvent', event)">
      <a>
        <i class="user icon"></i>
        Anzahl Teilnehmende: {{ event.participantCount }}
      </a>
    </div>
  </div>
</template>

<script setup lang="ts">

import { toRefs, defineEmits, defineProps } from 'vue'
import type { IEvent } from '../eventservice.ts'

import RemoveButton from './RemoveButton.vue'

const emit = defineEmits<{
  updateEvent: [event: IEvent]
  removeEvent: [event: IEvent]
}>()

const props = defineProps<{ event: IEvent, index: number }>()

const { event, index } = toRefs(props);

</script>