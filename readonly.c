#include<stdio.h>
#include<sys/mman.h>
#include<stdlib.h>
#include<unistd.h>
#include<string.h>

int main(int argc, char **argv) {
    system("clear");

    int page_size = sysconf(_SC_PAGE_SIZE);
    if(page_size == -1)
        perror("sysconf");

    printf("Page Size:\t%d\n", page_size);

    int buffer_size = 2 * page_size;
    char *p1 = malloc(sizeof(char) * 50);

    printf("Poniter 1:\t%p\n", p1);

    char *p2, *p3;
    if(posix_memalign((void **)&p2, page_size, buffer_size))
        perror("posix_memalign");

    if(posix_memalign((void **)&p3, page_size, buffer_size))
        perror("posix_memalign");

    p3 = mmap(NULL, buffer_size, PROT_READ | PROT_WRITE, MAP_ANONYMOUS | MAP_PRIVATE, -1, 0);
    //To protect memory block at p2 from beig written
    // p2 = mmap(NULL, buffer_size, PROT_READ, MAP_ANONYMOUS | MAP_PRIVATE, -1, 0);



    printf("Pointer 2:\t%p\n", p2);
    printf("Pointer 3:\t%p\n", p3);

    printf("\n");
    printf("[+] Writing on %p", p1);
    memset(p1, 5, buffer_size);
    printf("\n[+] Done.\n");

    printf("[+] Writing on %p", p3);
    memset(p3, 5, buffer_size);
    printf("\n[+] Done.\n");

    if(mprotect(p2 + page_size, page_size, PROT_READ) == -1)
        perror("mprotect");

    for (int i = 0; i < buffer_size; i++){
        printf("%d (%p): Writting... \n", i, p2 + i);
        p2[i] = i;
    }

    return EXIT_SUCCESS;
}
