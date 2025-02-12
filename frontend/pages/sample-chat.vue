<template>
  <div class="w-4/5 mx-auto">
    <div class="space-y-4">

      <Header
        :requestDummyData="requestDummyData"
        :toggleModal="toggleLogModal"
        :toggleDisplay="toggleDisplay"
      />

      <Content
        :displayMode="displayMode"
        :currentTranscription="currentTranscription"
        :currentSimplification="currentSimplification"
      />

    </div> 
  </div>

  <TranscriptionLogModal
        :isModalOpen="isModalOpen" 
        :transcriptions="transcriptions"
        @update:isModalOpen="isModalOpen = $event" 

/>
</template>

<script>
export default {
  data() {
    return {
      displayMode: 'horizontal', 
      isModalOpen: false,
      currentTranscription: '',
      currentSimplification: '',
      transcriptions: [],
      dummyIndex: 0,
      transcriptionIndex: 0, 
      simplificationIndex: 0, 
    };
  },

  mounted() {
      this.socket = this.$nuxtSocket({
        name: 'main',
        channel: '/'
      });
      this.socket.on('transcription', (data) => {
        console.log('Received transcript:', data);
        this.currentTranscription = data.message;
        this.transcriptions.push({
          text: data.message,
          date: new Date(),
        });
      });
      this.socket.on('simplification', (data) => {
        console.log('Received simplified transcript:', data);
        this.currentSimplification = data.message;
      });
  },
  computed: {
    layoutClass() {
      if (this.displayMode === 'horizontal') {
        return 'h-[80vh] w-full flex border-teal-500 border-4 rounded-2xl';
      } else {
        return 'space-y-4';
      }
    },
    sectionClass() {
      if (this.displayMode === 'horizontal') {
        return 'w-1/2 flex flex-col items-start';
      } else {
        return 'h-[40vh] w-full flex flex-col items-start border-teal-500 border-4 rounded-2xl';
      }
    },
  },
  methods: {
    toggleDisplay() {
      if (this.displayMode === 'horizontal') {
        this.displayMode = 'vertical';
      } else {
        this.displayMode = 'horizontal';
      }
    },
    toggleLogModal() {
      this.isModalOpen = !this.isModalOpen;
    },
    requestDummyData() {
      if (this.dummyIndex % 2 == 0) {
        this.requestTranscription();
      } else {
        this.requestSimplification();
      };
      this.dummyIndex++;
    },
    requestTranscription() {
        this.socket.emit('transcription', { message: this.transcriptionIndex });
        this.transcriptionIndex++;
    },
    requestSimplification() {
        this.socket.emit('simplification', { message: this.simplificationIndex });
        this.simplificationIndex++;
    },
  },
};
</script>