sql_alter_drop_commands="""
alter table ANGESTELLTER
   drop constraint FK_ANGESTEL_ABTEILUNG_ABTEILUN;

alter table ANGESTELLTER
   drop constraint FK_ANGESTEL_ANSTELLUN_ANGESTEL;

alter table BESTELLUNG
   drop constraint FK_BESTELLU_BESTELLUN_MERCHART;

alter table BESTELLUNG
   drop constraint FK_BESTELLU_LIEFERUNG_LIEFERAN;

alter table BESTELLUNG
   drop constraint FK_BESTELLU_SNACK___B_SNACK;

alter table KOMET
   drop constraint FK_KOMET_KOMET___G_GALAXIE;

alter table MEDIUM
   drop constraint FK_MEDIUM_MEDIUM____GALAXIE;

alter table MEDIUM
   drop constraint FK_MEDIUM_MEDIUM____KOMET;

alter table MEDIUM
   drop constraint FK_MEDIUM_MEDIUM____NEBEL;

alter table MEDIUM
   drop constraint FK_MEDIUM_MEDIUM____PLANET;

alter table MEDIUM
   drop constraint FK_MEDIUM_MEDIUM____PLANETEN;

alter table MEDIUM
   drop constraint FK_MEDIUM_MEDIUM____STERN;

alter table MEDIUM
   drop constraint FK_MEDIUM_MEDIUM____STERNENB;

alter table NEBEL
   drop constraint FK_NEBEL_GALAXIE___GALAXIE;

alter table PLANET
   drop constraint FK_PLANET_PLANET____PLANET;

alter table PLANET
   drop constraint FK_PLANET_PLANET____PLANETEN;

alter table PLANETENSYSTEM
   drop constraint FK_PLANETEN_GALAXIE___GALAXIE;

alter table RAUM
   drop constraint FK_RAUM_ABTEILUNG_ABTEILUN;

alter table STERN
   drop constraint FK_STERN_PLANTENSY_PLANETEN;

alter table STERN
   drop constraint FK_STERN_STERN___S_STERNENB;

alter table VERANSTALTUNG
   drop constraint FK_VERANSTA_RAUM___VE_RAUM;

alter table VERANSTALTUNG_ANGESTELLTER
   drop constraint FK_VERANSTA_LEITET_VERANSTA;

alter table VERANSTALTUNG_ANGESTELLTER
   drop constraint "FK_VERANSTA_WIRD GELE_ANGESTEL";

alter table VERANSTALTUNG_MEDIUM
   drop constraint FK_VERANSTA_ENTHAELT_MEDIUM;

alter table VERANSTALTUNG_MEDIUM
   drop constraint "FK_VERANSTA_WIRD VERW_VERANSTA";

alter table VERKAUF
   drop constraint FK_VERKAUF_ANGESTELL_ANGESTEL;

alter table VERKAUF
   drop constraint FK_VERKAUF_KUNDE___V_KUNDE;

alter table VERKAUF_MERCH
   drop constraint FK_VERKAUF__MERCHARTI_VERKAUF;

alter table VERKAUF_MERCH
   drop constraint FK_VERKAUF__ENTHAELT_MERCHART;

alter table VERKAUF_SNACK
   drop constraint "FK_VERKAUF__SNACK WIR_VERKAUF";

alter table VERKAUF_SNACK
   drop constraint FK_VERKAUF__VERKAUFT_SNACK;

alter table VERKAUF_TICKETSTUFE
   drop constraint "FK_VERKAUF__TICKET WI_VERKAUF";

alter table VERKAUF_TICKETSTUFE
   drop constraint FK_VERKAUF__ENTHAELT_TICKETST;

alter table VERMIETUNG_RAUM
   drop constraint "FK_VERMIETU_RAUM WIRD_KUNDE";

alter table VERMIETUNG_RAUM
   drop constraint FK_VERMIETU_MIETET_RAUM;

alter table VERMIETUNG_TELESKOP
   drop constraint "FK_VERMIETU_TELESKOP _KUNDE";

alter table VERMIETUNG_TELESKOP
   drop constraint FK_VERMIETU_MIETET_TELESKOP;

drop table ABTEILUNG cascade constraints;

drop index ABTEILUNG___ANGESTELLTER_FK;

drop index ANSTELLUNG_FK;

drop table ANGESTELLTER cascade constraints;

drop table BESTELLUNG cascade constraints;

drop table GALAXIE cascade constraints;

drop index KOMET___GALAXIE_FK;

drop table KOMET cascade constraints;

drop table KUNDE cascade constraints;

drop table LIEFERANT cascade constraints;

drop index MEDIUM___NEBEL_FK;

drop index MEDIUM___GALAXIE_FK;

drop index MEDIUM___KOMET_FK;

drop index MEDIUM___PLANET_FK;

drop index MEDIUM___PLANETENSYSTEM_FK;

drop index MEDIUM___STERN_FK;

drop index MEDIUM___STERNBILD_FK;

drop table MEDIUM cascade constraints;

drop table MERCHARTIKEL cascade constraints;

drop index GALAXIE___NEBEL_FK;

drop table NEBEL cascade constraints;

drop index RELATIONSHIP_32_FK;

drop index PLANET___PLANETENSYSTEM_FK;

drop table PLANET cascade constraints;

drop index GALAXIE___PLANETENSYSTEM_FK;

drop table PLANETENSYSTEM cascade constraints;

drop table RAUM cascade constraints;

drop table SNACK cascade constraints;

drop index STERN___STERNENBILD_FK;

drop index PLANTENSYSTEM___STERN_FK;

drop table STERN cascade constraints;

drop table STERNENBILD cascade constraints;

drop table TELESKOP cascade constraints;

drop table TICKETSTUFE cascade constraints;

drop index RAUM___VERANSTALTUNG_FK;

drop table VERANSTALTUNG cascade constraints;

drop index WIRD_GELEITET_FK;

drop index LEITET_FK;

drop table VERANSTALTUNG_ANGESTELLTER cascade constraints;

drop index ENTHALT_FK1;

drop index WIRD_VERWENDET_FK;

drop table VERANSTALTUNG_MEDIUM cascade constraints;

drop index ANGESTELLTER___VERKAUF_FK;

drop index KUNDE___VERKAUF_FK;

drop table VERKAUF cascade constraints;

drop index ENTHALT_FK;

drop index MERCH_WIRD_VERKAUFT_FK;

drop table VERKAUF_MERCH cascade constraints;

drop index VERKAUFT_FK;

drop index SNACK_WIRD_VERKAUFT_FK;

drop table VERKAUF_SNACK cascade constraints;

drop index ENTHALT_FK3;

drop index WIRD_VERKAUFT_FK3;

drop table VERKAUF_TICKETSTUFE cascade constraints;

drop index MIETET_RAUM_FK;

drop index RAUM_WIRD_GEMIETET_FK;

drop table VERMIETUNG_RAUM cascade constraints;

drop index MIETET_TELESKOP_FK;

drop index WIRD_GEMIETET_FK;

drop table VERMIETUNG_TELESKOP cascade constraints;
"""


sql_create_Tables="""
/*==============================================================*/
/* Table: ABTEILUNG                                             */
/*==============================================================*/
create table ABTEILUNG (
   ID                   NUMBER(8)             GENERATED ALWAYS AS IDENTITY not null,
   NAME                 VARCHAR2(100)         not null,
   BESCHREIBUNG         CLOB,
   constraint PK_ABTEILUNG primary key (ID)
);

/*==============================================================*/
/* Table: ANGESTELLTER                                          */
/*==============================================================*/
create table ANGESTELLTER (
   ID                   NUMBER(8)             GENERATED ALWAYS AS IDENTITY not null,
   CHEF_ID              NUMBER(8),
   ABTEILUNG_ID         NUMBER(8)             not null,
   NAME                 VARCHAR2(100)         not null,
   VORNAME              VARCHAR2(100)         not null,
   GEHALT               NUMBER(7,2)           not null,
   constraint PK_ANGESTELLTER primary key (ID),
   constraint FK_ANGESTEL_ANSTELLUN_ANGESTEL foreign key (CHEF_ID)
         references ANGESTELLTER (ID),
   constraint FK_ANGESTEL_ABTEILUNG_ABTEILUN foreign key (ABTEILUNG_ID)
         references ABTEILUNG (ID)
);

/*==============================================================*/
/* Index: ANSTELLUNG_FK                                         */
/*==============================================================*/
create index ANSTELLUNG_FK on ANGESTELLTER (
   CHEF_ID ASC
);

/*==============================================================*/
/* Index: ABTEILUNG___ANGESTELLTER_FK                           */
/*==============================================================*/
create index ABTEILUNG___ANGESTELLTER_FK on ANGESTELLTER (
   ABTEILUNG_ID ASC
);

/*==============================================================*/
/* Table: SNACK                                                 */
/*==============================================================*/
create table SNACK (
   ID                   NUMBER(8)            GENERATED ALWAYS AS IDENTITY (START WITH 2 INCREMENT BY 2 MINVALUE 2) not null,
   BEZEICHNUNG          VARCHAR2(100)         not null,
   BESCHREIBUNG         VARCHAR2(200)         not null,
   VERKAUF_PREIS_STK     NUMBER(5,2)           not null,
   GROESSE              CHAR(3)               check ((GROESSE in ('M','L') AND GROESSE = upper(GROESSE)) OR GROESSE is null),
   IMAGE_PATH           VARCHAR(100)           not null,
   constraint PK_SNACK primary key (ID)
);

/*==============================================================*/
/* Table: MERCHARTIKEL                                          */
/*==============================================================*/
create table MERCHARTIKEL (
   ID                   NUMBER(8)            GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 2 MINVALUE 1) not null,
   BEZEICHNUNG          VARCHAR2(100)         not null,
   BESCHREIBUNG         VARCHAR(200)          not null,
   GROESSE              CHAR(3)               check ((GROESSE in ('XS','S','M','L','XL','XXL') AND GROESSE = upper(GROESSE)) OR GROESSE is null),
   VERKAUF_PREIS_STK    NUMBER(5,2)           not null,
   IMAGE_PATH           VARCHAR(100)             not null,
   constraint PK_MERCHARTIKEL primary key (ID)
);

/*==============================================================*/
/* Table: LIEFERANT                                             */
/*==============================================================*/
create table LIEFERANT (
   ID                   NUMBER(8)            GENERATED ALWAYS AS IDENTITY not null,
   NAME                 VARCHAR2(100)         not null,
   constraint PK_LIEFERANT primary key (ID)
);

/*==============================================================*/
/* Table: BESTELLUNG                                            */
/*==============================================================*/
create table BESTELLUNG (
   ID                   NUMBER(8)            GENERATED ALWAYS AS IDENTITY not null,
   SNACK_ID             NUMBER(8),
   MERCHARTIKEL_ID      NUMBER(8),
   LIEFERANT_ID         NUMBER(8)             not null,
   ANZAHL               NUMBER(5)             not null,
   RABATT               NUMBER(5,2),
   ANKAUF_PREIS         NUMBER(5,2)           not null,
   constraint PK_BESTELLUNG primary key (ID),
   constraint FK_BESTELLU_SNACK___B_SNACK foreign key (SNACK_ID)
         references SNACK (ID),
   constraint FK_BESTELLU_BESTELLUN_MERCHART foreign key (MERCHARTIKEL_ID)
         references MERCHARTIKEL (ID),
   constraint FK_BESTELLU_LIEFERUNG_LIEFERAN foreign key (LIEFERANT_ID)
         references LIEFERANT (ID),
   constraint ONLY_ONE_NOT_NULL check ((SNACK_ID is not null AND MERCHARTIKEL_ID is null) OR (SNACK_ID is null AND MERCHARTIKEL_ID is not null))
);

/*==============================================================*/
/* Table: GALAXIE                                               */
/*==============================================================*/
create table GALAXIE (
   ID                   NUMBER(8)            GENERATED ALWAYS AS IDENTITY not null,
   NAME                 VARCHAR2(100)         not null,
   DURCHMESSER_LJ       FLOAT,
   MASSE_KG             FLOAT,
   ENTFERNUNG_LJ        FLOAT,
   INFORMATIONEN        CLOB,
   constraint PK_GALAXIE primary key (ID)
);

/*==============================================================*/
/* Table: KOMET                                                 */
/*==============================================================*/
create table KOMET (
   ID                   NUMBER(8)            GENERATED ALWAYS AS IDENTITY not null,
   GALAXIE_ID           NUMBER(8)             not null,
   NAME                 VARCHAR2(100)         not null,
   DURCHMESSER_KM       FLOAT,
   MASSE_KG             FLOAT,
   UMLAUFZEIT_J         FLOAT,
   INFORMATIONEN          CLOB,
   constraint PK_KOMET primary key (ID),
   constraint FK_KOMET_KOMET___G_GALAXIE foreign key (GALAXIE_ID)
         references GALAXIE (ID)
);

/*==============================================================*/
/* Index: KOMET___GALAXIE_FK                                    */
/*==============================================================*/
create index KOMET___GALAXIE_FK on KOMET (
   GALAXIE_ID ASC
);

/*==============================================================*/
/* Table: KUNDE                                                 */
/*==============================================================*/
create table KUNDE (
   ID                   NUMBER(8)            GENERATED ALWAYS AS IDENTITY not null,
   NAME                 VARCHAR2(100)         default 'Gast'  not null,
   VORNAME              VARCHAR2(100)         default 'Gast'  not null,
   TELEFON_NR           VARCHAR2(20)          default '+0000000000000000000'  not null,
   EMAIL                VARCHAR2(100)         default 'gast.gast@gast.com'  not null,
   constraint PK_KUNDE primary key (ID)
);

/*==============================================================*/
/* Table: STERNENBILD                                           */
/*==============================================================*/
create table STERNENBILD (
   ID                   NUMBER(8)            GENERATED ALWAYS AS IDENTITY not null,
   NAME                 VARCHAR2(100)         not null,
   ANZAHL_STERNE        INTEGER,
   INFORMATIONEN        CLOB,
   constraint PK_STERNENBILD primary key (ID)
);

/*==============================================================*/
/* Table: PLANETENSYSTEM                                        */
/*==============================================================*/
create table PLANETENSYSTEM (
   ID                   NUMBER(8)            GENERATED ALWAYS AS IDENTITY not null,
   GALAXIE_ID           NUMBER(8)             not null,
   NAME                 VARCHAR2(100)         not null,
   INFORMATIONEN        CLOB,
   constraint PK_PLANETENSYSTEM primary key (ID),
   constraint FK_PLANETEN_GALAXIE___GALAXIE foreign key (GALAXIE_ID)
         references GALAXIE (ID)
);

/*==============================================================*/
/* Table: STERN                                                 */
/*==============================================================*/
create table STERN (
   ID                   NUMBER(8)            GENERATED ALWAYS AS IDENTITY not null,
   STERNENBILD_ID       NUMBER(8),
   PLANETENSYSTEM_ID    NUMBER(8),
   NAME                 VARCHAR2(100)         not null,
   TYP                  VARCHAR2(100),
   DURCHMESSER_KM       FLOAT,
   MASSE_KG             FLOAT,
   ENTFERNUNG_LJ        FLOAT,
   INFORMATIONEN        CLOB,
   constraint PK_STERN primary key (ID),
   constraint FK_STERN_PLANTENSY_PLANETEN foreign key (PLANETENSYSTEM_ID)
         references PLANETENSYSTEM (ID),
   constraint FK_STERN_STERN___S_STERNENB foreign key (STERNENBILD_ID)
         references STERNENBILD (ID)
);

/*==============================================================*/
/* Table: PLANET                                                */
/*==============================================================*/
create table PLANET (
   ID                   NUMBER(8)            GENERATED ALWAYS AS IDENTITY not null,
   PLANETENSYSTEM_ID    NUMBER(8),
   ZENTRUMSPLANET_ID    NUMBER(8),
   NAME                 VARCHAR2(100)         not null,
   DURCHMESSER_KM       FLOAT,
   MASSE_KG             FLOAT,
   UMLAUFZEIT_TAGE      FLOAT,
   TEMPERATUR_CELSIUS   FLOAT,
   FALLBESCHLEUNIGUNG   FLOAT,
   INFORMATIONEN        CLOB,
   constraint PK_PLANET primary key (ID),
   constraint FK_PLANET_PLANET____PLANETEN foreign key (PLANETENSYSTEM_ID)
         references PLANETENSYSTEM (ID),
   constraint FK_PLANET_PLANET____PLANET foreign key (ZENTRUMSPLANET_ID)
         references PLANET (ID)
);

/*==============================================================*/
/* Table: NEBEL                                                 */
/*==============================================================*/
create table NEBEL (
   ID                   NUMBER(8)            GENERATED ALWAYS AS IDENTITY not null,
   GALAXIE_ID           NUMBER(8)             not null,
   NAME                 VARCHAR2(100)         not null,
   DURCHMESSER_LJ       FLOAT,
   MASSE_KG             FLOAT,
   ENTFERNUNG_LJ        FLOAT,
   INFORMATIONEN        CLOB,
   constraint PK_NEBEL primary key (ID),
   constraint FK_NEBEL_GALAXIE___GALAXIE foreign key (GALAXIE_ID)
         references GALAXIE (ID)
);

/*==============================================================*/
/* Table: MEDIUM                                                */
/*==============================================================*/
create table MEDIUM (
   ID                   NUMBER(8)            GENERATED ALWAYS AS IDENTITY not null,
   GALAXIE_ID           NUMBER(8),
   PLANET_ID            NUMBER(8),
   PLANETENSYSTEM_ID    NUMBER(8),
   NEBEL_ID             NUMBER(8),
   STERN_ID             NUMBER(8),
   STERNENBILD_ID       NUMBER(8),
   KOMET_ID             NUMBER(8),
   FORMAT               CHAR(6)               not null,
   TYP                  CHAR(10)              check (TYP in ('Video','Bild','Audio','3D-Modell','Dokument')) not null,
   IMAGE_PATH           VARCHAR(100)             not null,
   constraint PK_MEDIUM primary key (ID),
   constraint FK_MEDIUM_MEDIUM____STERNENB foreign key (STERN_ID)
         references STERNENBILD (ID),
   constraint FK_MEDIUM_MEDIUM____STERN foreign key (STERNENBILD_ID)
         references STERN (ID),
   constraint FK_MEDIUM_MEDIUM____PLANETEN foreign key (PLANETENSYSTEM_ID)
         references PLANETENSYSTEM (ID),
   constraint FK_MEDIUM_MEDIUM____PLANET foreign key (PLANET_ID)
         references PLANET (ID),
   constraint FK_MEDIUM_MEDIUM____KOMET foreign key (KOMET_ID)
         references KOMET (ID),
   constraint FK_MEDIUM_MEDIUM____GALAXIE foreign key (GALAXIE_ID)
         references GALAXIE (ID),
   constraint FK_MEDIUM_MEDIUM____NEBEL foreign key (NEBEL_ID)
         references NEBEL (ID)
);

/*==============================================================*/
/* Index: MEDIUM___STERNBILD_FK                                 */
/*==============================================================*/
create index MEDIUM___STERNBILD_FK on MEDIUM (
   STERN_ID ASC
);

/*==============================================================*/
/* Index: MEDIUM___STERN_FK                                     */
/*==============================================================*/
create index MEDIUM___STERN_FK on MEDIUM (
   STERNENBILD_ID ASC
);

/*==============================================================*/
/* Index: MEDIUM___PLANETENSYSTEM_FK                            */
/*==============================================================*/
create index MEDIUM___PLANETENSYSTEM_FK on MEDIUM (
   PLANETENSYSTEM_ID ASC
);

/*==============================================================*/
/* Index: MEDIUM___PLANET_FK                                    */
/*==============================================================*/
create index MEDIUM___PLANET_FK on MEDIUM (
   PLANET_ID ASC
);

/*==============================================================*/
/* Index: MEDIUM___KOMET_FK                                     */
/*==============================================================*/
create index MEDIUM___KOMET_FK on MEDIUM (
   KOMET_ID ASC
);

/*==============================================================*/
/* Index: MEDIUM___GALAXIE_FK                                   */
/*==============================================================*/
create index MEDIUM___GALAXIE_FK on MEDIUM (
   GALAXIE_ID ASC
);

/*==============================================================*/
/* Index: MEDIUM___NEBEL_FK                                  */
/*==============================================================*/
create index MEDIUM___NEBEL_FK on MEDIUM (
   NEBEL_ID ASC
);

/*==============================================================*/
/* Index: GALAXIE___NEBEL_FK                                 */
/*==============================================================*/
create index GALAXIE___NEBEL_FK on NEBEL (
   GALAXIE_ID ASC
);

/*==============================================================*/
/* Index: PLANET___PLANETENSYSTEM_FK                            */
/*==============================================================*/
create index PLANET___PLANETENSYSTEM_FK on PLANET (
   PLANETENSYSTEM_ID ASC
);

/*==============================================================*/
/* Index: RELATIONSHIP_32_FK                                    */
/*==============================================================*/
create index RELATIONSHIP_32_FK on PLANET (
   ZENTRUMSPLANET_ID ASC
);

/*==============================================================*/
/* Index: GALAXIE___PLANETENSYSTEM_FK                           */
/*==============================================================*/
create index GALAXIE___PLANETENSYSTEM_FK on PLANETENSYSTEM (
   GALAXIE_ID ASC
);

/*==============================================================*/
/* Table: RAUM                                                  */
/*==============================================================*/
create table RAUM (
   ID                   NUMBER(8)            GENERATED ALWAYS AS IDENTITY not null,
   ABTEILUNG_ID         NUMBER(8),
   BEZEICHNUNG          VARCHAR2(100)         not null,
   KAPAZITAT            NUMBER(3)             not null,
   MIET_PREIS           NUMBER(5,2),
   constraint PK_RAUM primary key (ID),
   constraint FK_RAUM_ABTEILUNG_ABTEILUN foreign key (ABTEILUNG_ID)
         references ABTEILUNG (ID)
);

/*==============================================================*/
/* Index: PLANTENSYSTEM___STERN_FK                              */
/*==============================================================*/
create index PLANTENSYSTEM___STERN_FK on STERN (
   PLANETENSYSTEM_ID ASC
);

/*==============================================================*/
/* Index: STERN___STERNENBILD_FK                                */
/*==============================================================*/
create index STERN___STERNENBILD_FK on STERN (
   STERNENBILD_ID ASC
);

/*==============================================================*/
/* Table: TELESKOP                                              */
/*==============================================================*/
create table TELESKOP (
   ID                   NUMBER(8)            GENERATED ALWAYS AS IDENTITY not null,
   BEZEICHNUNG          VARCHAR2(100)         not null,
   TYP                  VARCHAR2(100)         not null,
   TAGES_MIET_PREIS     NUMBER(5,2),
   BESCHREIBUNG         CLOB,
   constraint PK_TELESKOP primary key (ID)
);

/*==============================================================*/
/* Table: TICKETSTUFE                                           */
/*==============================================================*/
create table TICKETSTUFE (
   STUFE                VARCHAR2(20)              default 'Tag' check (STUFE in ('Tag','Monat','Jahr')) not null,
   ZEITRAUM             NUMBER(3)             default 1 check (ZEITRAUM between 1 and 365 and ZEITRAUM in (1,30,365)) not null,
   PREIS                NUMBER(5,2)           not null,
   IMAGE_PATH           VARCHAR2(100)          not null,
   constraint PK_TICKETSTUFE primary key (STUFE),
   constraint MATCHING_STUFE_ZEITRAUM check((STUFE = 'Tag' AND ZEITRAUM = 1) OR (STUFE = 'Monat' AND ZEITRAUM = 30) OR (STUFE = 'Jahr' AND ZEITRAUM = 365))
);

/*==============================================================*/
/* Table: VERANSTALTUNG                                         */
/*==============================================================*/
create table VERANSTALTUNG (
   ID                   NUMBER(8)            GENERATED ALWAYS AS IDENTITY not null,
   RAUM_ID              NUMBER(8)             not null,
   NAME                 VARCHAR2(100)         not null,
   DATUM                DATE                  not null,
   BESCHREIBUNG         CLOB,
   constraint PK_VERANSTALTUNG primary key (ID),
   constraint FK_VERANSTA_RAUM___VE_RAUM foreign key (RAUM_ID)
         references RAUM (ID)
);

/*==============================================================*/
/* Index: RAUM___VERANSTALTUNG_FK                               */
/*==============================================================*/
create index RAUM___VERANSTALTUNG_FK on VERANSTALTUNG (
   RAUM_ID ASC
);

/*==============================================================*/
/* Table: VERANSTALTUNG_ANGESTELLTER                            */
/*==============================================================*/
create table VERANSTALTUNG_ANGESTELLTER (
   VERANSTALTUNG_ID     NUMBER(8)             not null,
   ANGESTELLTER_ID      NUMBER(8)             not null,
   constraint PK_VERANSTALTUNG_ANGESTELLTER primary key (VERANSTALTUNG_ID, ANGESTELLTER_ID),
   constraint FK_VERANSTA_LEITET_VERANSTA foreign key (VERANSTALTUNG_ID)
         references VERANSTALTUNG (ID),
   constraint "FK_VERANSTA_WIRD GELE_ANGESTEL" foreign key (ANGESTELLTER_ID)
         references ANGESTELLTER (ID)
);

/*==============================================================*/
/* Index: LEITET_FK                                             */
/*==============================================================*/
create index LEITET_FK on VERANSTALTUNG_ANGESTELLTER (
   VERANSTALTUNG_ID ASC
);

/*==============================================================*/
/* Index: WIRD_GELEITET_FK                                      */
/*==============================================================*/
create index WIRD_GELEITET_FK on VERANSTALTUNG_ANGESTELLTER (
   ANGESTELLTER_ID ASC
);

/*==============================================================*/
/* Table: VERANSTALTUNG_MEDIUM                                  */
/*==============================================================*/
create table VERANSTALTUNG_MEDIUM (
   VERANSTALTUNG_ID     NUMBER(8)             not null,
   MEDIUM_ID            NUMBER(8)             not null,
   constraint PK_VERANSTALTUNG_MEDIUM primary key (VERANSTALTUNG_ID, MEDIUM_ID),
   constraint "FK_VERANSTA_WIRD VERW_VERANSTA" foreign key (VERANSTALTUNG_ID)
         references VERANSTALTUNG (ID),
   constraint FK_VERANSTA_ENTHAELT_MEDIUM foreign key (MEDIUM_ID)
         references MEDIUM (ID)
);

/*==============================================================*/
/* Index: WIRD_VERWENDET_FK                                     */
/*==============================================================*/
create index WIRD_VERWENDET_FK on VERANSTALTUNG_MEDIUM (
   VERANSTALTUNG_ID ASC
);

/*==============================================================*/
/* Index: ENTHALT_FK1                                           */
/*==============================================================*/
create index ENTHALT_FK1 on VERANSTALTUNG_MEDIUM (
   MEDIUM_ID ASC
);

/*==============================================================*/
/* Table: VERKAUF                                               */
/*==============================================================*/
create table VERKAUF (
   ID                   NUMBER(8)            GENERATED ALWAYS AS IDENTITY not null,
   KUNDE_ID             NUMBER(8)             not null,
   ANGESTELLTER_ID      NUMBER(8)             not null,
   RABATT               NUMBER(3,2),
   DATUM                DATE                  not null,
   constraint PK_VERKAUF primary key (ID),
   constraint FK_VERKAUF_KUNDE___V_KUNDE foreign key (KUNDE_ID)
         references KUNDE (ID),
   constraint FK_VERKAUF_ANGESTELL_ANGESTEL foreign key (ANGESTELLTER_ID)
         references ANGESTELLTER (ID)
);

/*==============================================================*/
/* Index: KUNDE___VERKAUF_FK                                    */
/*==============================================================*/
create index KUNDE___VERKAUF_FK on VERKAUF (
   KUNDE_ID ASC
);

/*==============================================================*/
/* Index: ANGESTELLTER___VERKAUF_FK                             */
/*==============================================================*/
create index ANGESTELLTER___VERKAUF_FK on VERKAUF (
   ANGESTELLTER_ID ASC
);

/*==============================================================*/
/* Table: VERKAUF_MERCH                                         */
/*==============================================================*/
create table VERKAUF_MERCH (
   VERKAUF_ID           NUMBER(8)             not null,
   MERCHARTIKEL_ID      NUMBER(8)             not null,
   ANZAHL               NUMBER(2)             not null,
   constraint PK_VERKAUF_MERCH primary key (VERKAUF_ID, MERCHARTIKEL_ID),
   constraint FK_VERKAUF__MERCHARTI_VERKAUF foreign key (VERKAUF_ID)
         references VERKAUF (ID),
   constraint FK_VERKAUF__ENTHAELT_MERCHART foreign key (MERCHARTIKEL_ID)
         references MERCHARTIKEL (ID)
);

/*==============================================================*/
/* Index: MERCH_WIRD_VERKAUFT_FK                                */
/*==============================================================*/
create index MERCH_WIRD_VERKAUFT_FK on VERKAUF_MERCH (
   VERKAUF_ID ASC
);

/*==============================================================*/
/* Index: ENTHALT_FK                                            */
/*==============================================================*/
create index ENTHALT_FK on VERKAUF_MERCH (
   MERCHARTIKEL_ID ASC
);

/*==============================================================*/
/* Table: VERKAUF_SNACK                                         */
/*==============================================================*/
create table VERKAUF_SNACK (
   VERKAUF_ID           NUMBER(8)             not null,
   SNACK_ID             NUMBER(8)             not null,
   ANZAHL               NUMBER(2)             not null,
   constraint PK_VERKAUF_SNACK primary key (VERKAUF_ID, SNACK_ID),
   constraint "FK_VERKAUF__SNACK WIR_VERKAUF" foreign key (VERKAUF_ID)
         references VERKAUF (ID),
   constraint FK_VERKAUF__VERKAUFT_SNACK foreign key (SNACK_ID)
         references SNACK (ID)
   );

/*==============================================================*/
/* Index: SNACK_WIRD_VERKAUFT_FK                                */
/*==============================================================*/
create index SNACK_WIRD_VERKAUFT_FK on VERKAUF_SNACK (
   VERKAUF_ID ASC
);

/*==============================================================*/
/* Index: VERKAUFT_FK                                           */
/*==============================================================*/
create index VERKAUFT_FK on VERKAUF_SNACK (
   SNACK_ID ASC
);

/*==============================================================*/
/* Table: VERKAUF_TICKETSTUFE                                   */
/*==============================================================*/
create table VERKAUF_TICKETSTUFE (
   VERKAUF_ID           NUMBER(8)             not null,
   STUFE                CHAR(20)              default 'Tag' check (STUFE in ('Tag','Monat','Jahr')) not null,
   ANZAHL               NUMBER(2)             not null,
   constraint PK_VERKAUF_TICKETSTUFE primary key (VERKAUF_ID, STUFE),
   constraint "FK_VERKAUF__TICKET WI_VERKAUF" foreign key (VERKAUF_ID)
         references VERKAUF (ID),
   constraint FK_VERKAUF__ENTHAELT_TICKETST foreign key (STUFE)
         references TICKETSTUFE (STUFE)
);

/*==============================================================*/
/* Index: WIRD_VERKAUFT_FK3                                     */
/*==============================================================*/
create index WIRD_VERKAUFT_FK3 on VERKAUF_TICKETSTUFE (
   VERKAUF_ID ASC
);

/*==============================================================*/
/* Index: ENTHALT_FK3                                           */
/*==============================================================*/
create index ENTHALT_FK3 on VERKAUF_TICKETSTUFE (
   STUFE ASC
);

/*==============================================================*/
/* Table: VERMIETUNG_RAUM                                       */
/*==============================================================*/
create table VERMIETUNG_RAUM (
   KUNDE_ID             NUMBER(8)             not null,
   RAUM_ID              NUMBER(8)             not null,
   DATUM                DATE                  not null,
   DAUER_TAGE           INTEGER               default 1 check (DAUER_TAGE between 1 and 7) not null,
   constraint PK_VERMIETUNG_RAUM primary key (KUNDE_ID, RAUM_ID),
   constraint "FK_VERMIETU_RAUM WIRD_KUNDE" foreign key (KUNDE_ID)
         references KUNDE (ID),
   constraint FK_VERMIETU_MIETET_RAUM foreign key (RAUM_ID)
         references RAUM (ID)
);

/*==============================================================*/
/* Index: RAUM_WIRD_GEMIETET_FK                                 */
/*==============================================================*/
create index RAUM_WIRD_GEMIETET_FK on VERMIETUNG_RAUM (
   KUNDE_ID ASC
);

/*==============================================================*/
/* Index: MIETET_RAUM_FK                                        */
/*==============================================================*/
create index MIETET_RAUM_FK on VERMIETUNG_RAUM (
   RAUM_ID ASC
);

/*==============================================================*/
/* Table: VERMIETUNG_TELESKOP                                   */
/*==============================================================*/
create table VERMIETUNG_TELESKOP (
   KUNDE_ID             NUMBER(8)             not null,
   TELESKOP_ID          NUMBER(8)             not null,
   DATUM                DATE                  not null,
   DAUER_TAGE           INTEGER               default 1 check (DAUER_TAGE between 1 and 7) not null,
   constraint PK_VERMIETUNG_TELESKOP primary key (KUNDE_ID, TELESKOP_ID),
   constraint "FK_VERMIETU_TELESKOP _KUNDE" foreign key (KUNDE_ID)
         references KUNDE (ID),
   constraint FK_VERMIETU_MIETET_TELESKOP foreign key (TELESKOP_ID)
         references TELESKOP (ID)
);

/*==============================================================*/
/* Index: WIRD_GEMIETET_FK                                      */
/*==============================================================*/
create index WIRD_GEMIETET_FK on VERMIETUNG_TELESKOP (
   KUNDE_ID ASC
);

/*==============================================================*/
/* Index: MIETET_TELESKOP_FK                                    */
/*==============================================================*/
create index MIETET_TELESKOP_FK on VERMIETUNG_TELESKOP (
   TELESKOP_ID ASC
);
"""

sql_create_Views="""
-- View zur Anzeige der aktuell nicht vermieteten Räume
CREATE VIEW FREIE_RAEUME AS
SELECT RAUM.id, RAUM.bezeichnung, RAUM.kapazitat, RAUM.miet_preis
FROM RAUM LEFT JOIN VERMIETUNG_RAUM ON RAUM.id = VERMIETUNG_RAUM.raum_id
WHERE RAUM.miet_preis IS NOT NULL AND (VERMIETUNG_RAUM.datum + VERMIETUNG_RAUM.dauer_tage) < current_date
GROUP BY RAUM.id, RAUM.bezeichnung, RAUM.kapazitat, RAUM.miet_preis
ORDER BY RAUM.id;

-- View zur Anzeige des aktuellen Bestands der Snacks
CREATE VIEW BESTAENDE_SNACK AS
SELECT SNACK.id, SNACK.bezeichnung, SNACK.groesse, (SUM(BESTELLUNG.anzahl) - SUM(VERKAUF_SNACK.anzahl)) AS BESTAND
FROM SNACK 
LEFT JOIN BESTELLUNG ON SNACK.id = BESTELLUNG.snack_id
LEFT JOIN VERKAUF_SNACK ON SNACK.id = VERKAUF_SNACK.snack_id
GROUP BY SNACK.id, SNACK.bezeichnung, SNACK.groesse
ORDER BY SNACK.id;

-- View zur Anzeige des aktuellen Bestands der Merchartikel
CREATE VIEW BESTAENDE_MERCH AS
SELECT MERCHARTIKEL.id, MERCHARTIKEL.bezeichnung, MERCHARTIKEL.groesse, (SUM(BESTELLUNG.anzahl) - SUM(VERKAUF_MERCH.anzahl)) AS BESTAND
FROM MERCHARTIKEL 
LEFT JOIN BESTELLUNG ON MERCHARTIKEL.id = BESTELLUNG.MERCHARTIKEL_ID
LEFT JOIN VERKAUF_MERCH ON MERCHARTIKEL.id = VERKAUF_MERCH.merchartikel_id
GROUP BY MERCHARTIKEL.id, MERCHARTIKEL.bezeichnung, MERCHARTIKEL.groesse
ORDER BY MERCHARTIKEL.id;

-- View zur Anzeige der Medien 
CREATE VIEW MEDIUM_VIEW AS
SELECT 
    galaxie.name AS galaxie_name, 
    planet.name AS planet_name, 
    planetensystem.name AS planetensystem_name, 
    nebel.name AS nebel_name, 
    stern.name AS stern_name, 
    sternenbild.name AS sternenbild_name, 
    komet.name AS komet_name, 
    MEDIUM.FORMAT, 
    MEDIUM.TYP,
    MEDIUM.image_path
FROM MEDIUM
LEFT JOIN GALAXIE 
ON MEDIUM.GALAXIE_ID = GALAXIE.ID
LEFT JOIN PLANET 
ON MEDIUM.PLANET_ID = PLANET.ID
LEFT JOIN PLANETENSYSTEM 
ON MEDIUM.PLANETENSYSTEM_ID = PLANETENSYSTEM.ID
LEFT JOIN NEBEL 
ON MEDIUM.NEBEL_ID = NEBEL.ID
LEFT JOIN STERN 
ON MEDIUM.STERN_ID = STERN.ID
LEFT JOIN STERNENBILD 
ON MEDIUM.STERNENBILD_ID = STERNENBILD.ID
LEFT JOIN KOMET 
ON MEDIUM.KOMET_ID = KOMET.ID;




CREATE VIEW GET_MERCH_CLOTHING AS
SELECT MERCHARTIKEL.id, MERCHARTIKEL.bezeichnung, MERCHARTIKEL.verkauf_preis_stk, MERCHARTIKEL.image_path, MERCHARTIKEL.beschreibung, MERCHARTIKEL.groesse 
FROM MERCHARTIKEL 
WHERE bezeichnung LIKE '%Hoodie%' OR bezeichnung LIKE '%Shirt%' OR bezeichnung LIKE '%Sock%' OR bezeichnung LIKE '%Vest%';

CREATE VIEW GET_MERCH_ACCESSOIRES AS
SELECT MERCHARTIKEL.id, MERCHARTIKEL.bezeichnung, MERCHARTIKEL.verkauf_preis_stk, MERCHARTIKEL.image_path, MERCHARTIKEL.beschreibung, MERCHARTIKEL.groesse 
FROM MERCHARTIKEL 
WHERE beschreibung LIKE '%brille%' OR beschreibung LIKE '%Magnet%' OR beschreibung LIKE '%Stick%';

CREATE VIEW GET_MERCH_HOUSEHOLDITEM AS
SELECT MERCHARTIKEL.id, MERCHARTIKEL.bezeichnung, MERCHARTIKEL.verkauf_preis_stk, MERCHARTIKEL.image_path, MERCHARTIKEL.beschreibung, MERCHARTIKEL.groesse 
FROM MERCHARTIKEL 
WHERE beschreibung LIKE '%tasse%' OR beschreibung LIKE '%vase%' OR beschreibung LIKE '%set%';

CREATE VIEW GET_MERCH_STATIONERY AS
SELECT MERCHARTIKEL.id, MERCHARTIKEL.bezeichnung, MERCHARTIKEL.verkauf_preis_stk, MERCHARTIKEL.image_path, MERCHARTIKEL.beschreibung, MERCHARTIKEL.groesse 
FROM MERCHARTIKEL 
WHERE beschreibung LIKE '%Skizze%';

CREATE VIEW GET_MERCH_OTHER AS
SELECT MERCHARTIKEL.id, MERCHARTIKEL.bezeichnung, MERCHARTIKEL.verkauf_preis_stk, MERCHARTIKEL.image_path, MERCHARTIKEL.beschreibung, MERCHARTIKEL.groesse 
FROM MERCHARTIKEL 
WHERE beschreibung LIKE '%schirm%';



CREATE VIEW GET_SNACK_DRINKS AS
SELECT SNACK.id, SNACK.bezeichnung, SNACK.beschreibung, SNACK.verkauf_preis_stk, SNACK.image_path, SNACK.groesse 
FROM SNACK 
WHERE bezeichnung LIKE '%Coke%' OR bezeichnung LIKE '%IceTea%' OR bezeichnung LIKE '%Beer%' OR bezeichnung LIKE '%Sprite%';

CREATE VIEW GET_SNACK_SWEET AS
SELECT SNACK.id, SNACK.bezeichnung, SNACK.beschreibung, SNACK.verkauf_preis_stk, SNACK.image_path, SNACK.groesse 
FROM SNACK 
WHERE bezeichnung LIKE '%Sugar%' OR bezeichnung LIKE '%Gummi%' OR bezeichnung LIKE '%Sweet%' OR beschreibung LIKE '%süß%' OR beschreibung LIKE '%Zucker%';

CREATE VIEW GET_SNACK_SALTY AS
SELECT SNACK.id, SNACK.bezeichnung, SNACK.beschreibung, SNACK.verkauf_preis_stk, SNACK.image_path, SNACK.groesse 
FROM SNACK 
WHERE beschreibung LIKE '%chips%' OR beschreibung LIKE '%salz%' OR beschreibung LIKE '%würzig%';



CREATE VIEW VERANSTALTUNG_TAG AS
SELECT id, raum_id, name, datum, beschreibung
FROM veranstaltung
WHERE datum = CURRENT_DATE;

CREATE VIEW VERANSTALTUNG_MONAT AS
SELECT id, raum_id, name, datum, beschreibung
FROM veranstaltung
WHERE datum BETWEEN CURRENT_DATE AND CURRENT_DATE + INTERVAL '30' DAY;

CREATE VIEW VERANSTALTUNG_JAHR AS
SELECT id, raum_id, name, datum, beschreibung
FROM VERANSTALTUNG
WHERE datum BETWEEN CURRENT_DATE AND CURRENT_DATE + INTERVAL '1' YEAR;


"""

sql_create_storedProcedure="""
-- Stored Procedure zur Verbuchung von verkauften Merchartikeln
CREATE OR REPLACE PROCEDURE VERKAUFEN_MERCH (
    p_merchartikel_id IN MERCHARTIKEL.id%TYPE,
    p_verkauf_anzahl IN VERKAUF_MERCH.anzahl%TYPE
) AS
    verkauf_id ASTROSPHERE.VERKAUF.id%TYPE;
BEGIN
    -- Verkauf verbuchen
    INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
    (1, 1, NULL, CURRENT_DATE);

    SELECT MAX(VERKAUF.id) INTO verkauf_id FROM ASTROSPHERE.VERKAUF;

    INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
    (verkauf_id, p_merchartikel_id, p_verkauf_anzahl);

    COMMIT; -- Transaktion abschließen
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        RAISE_APPLICATION_ERROR(-20001, 'Merchartikel ID nicht gefunden.');
    WHEN OTHERS THEN
        RAISE_APPLICATION_ERROR(-20002, 'Fehler beim Verkauf.');
END VERKAUFEN_MERCH;
/

-- Stored Procedure zur Verbuchung von verkauften Snacks
CREATE OR REPLACE PROCEDURE VERKAUFEN_SNACK (
    p_snack_id IN SNACK.id%TYPE,
    p_verkauf_anzahl IN VERKAUF_SNACK.anzahl%TYPE
) AS
    verkauf_id ASTROSPHERE.VERKAUF.id%TYPE;
BEGIN
    -- Verkauf verbuchen
    INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
    (1, 1, NULL, CURRENT_DATE);

    SELECT MAX(VERKAUF.id) INTO verkauf_id FROM ASTROSPHERE.VERKAUF;

    INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
    (verkauf_id, p_snack_id, p_verkauf_anzahl);

    COMMIT; -- Transaktion abschließen
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        RAISE_APPLICATION_ERROR(-20001, 'Snack ID nicht gefunden.');
    WHEN OTHERS THEN
        RAISE_APPLICATION_ERROR(-20002, 'Fehler beim Verkauf.');
END VERKAUFEN_SNACK;
/

-- Stored Procedure zur Suche von Räumen nach Bezeichnung
CREATE OR REPLACE PROCEDURE SUCHE_RAUM_BEZEICHNUNG (
    p_raum_bezeichnung IN RAUM.bezeichnung%TYPE
) 
BEGIN
   SELECT * FROM RAUM WHERE LIKE %p_raum_bezeichnung%;
    COMMIT;
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        RAISE_APPLICATION_ERROR(-20001, 'Raum Bezeichnung nicht gefunden.');
    WHEN OTHERS THEN
        RAISE_APPLICATION_ERROR(-20002, 'Fehler beim Suchen.');
END SUCHE_RAUM_BEZEICHNUNG;
/

-- Stored Procedure zur Suche von Räumen nach Bezeichnung
CREATE OR REPLACE PROCEDURE SUCHE_RAUM_KAPAZITAET (
    p_raum_kapazitat IN RAUM.kapazitat%TYPE
) 
BEGIN
   SELECT * FROM RAUM WHERE RAUM.kapazitat >= p_raum_kapazitat;
    COMMIT;
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        RAISE_APPLICATION_ERROR(-20001, 'Raum mit ausreichender Kapazitaet nicht gefunden.');
    WHEN OTHERS THEN
        RAISE_APPLICATION_ERROR(-20002, 'Fehler beim Suchen.');
END SUCHE_RAUM_BEZEICHNUNG;
/

CREATE OR REPLACE PROCEDURE GET_FREIE_RAUME (
   p_datum IN VERMIETUNG_RAUM_preis%TYPE
) AS 
BEGIN
   CREATE VIEW GET_FREIE_RAUME_NACH_DATUM 
   AS
   SELECT RAUM.id, RAUM.bezeichnung, RAUM.kapazitat, RAUM.miet_preis
   FROM RAUM LEFT JOIN VERMIETUNG_RAUM ON RAUM.id = VERMIETUNG_RAUM.raum_id
   WHERE RAUM.miet_preis IS NOT NULL AND (VERMIETUNG_RAUM.datum + VERMIETUNG_RAUM.dauer_tage) < p_datum
   GROUP BY RAUM.id, RAUM.bezeichnung, RAUM.kapazitat, RAUM.miet_preis
   ORDER BY RAUM.id;
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        RAISE_APPLICATION_ERROR(-20001, 'freier Raum nicht gefunden.');
    WHEN OTHERS THEN
        RAISE_APPLICATION_ERROR(-20002, 'Fehler beim Suchen.');
END GET_FREIE_RAUME;
"""

sql_configuration="""
SET SQLBLANKLINES ON;
SET DEFINE OFF;
ALTER SESSION SET NLS_DATE_FORMAT = 'MM/DD/SYYYY HH24:MI:SS';
ALTER SESSION SET NLS_TIMESTAMP_TZ_FORMAT = 'MM/DD/SYYYY HH24:MI:SS.FF TZH:TZM';
ALTER SESSION SET NLS_TIMESTAMP_FORMAT = 'MM/DD/SYYYY HH24:MI:SS.FF';
ALTER SESSION SET NLS_NUMERIC_CHARACTERS = '.,';
ALTER SESSION SET NLS_NCHAR_CONV_EXCP = FALSE;
ALTER SESSION SET TIME_ZONE = '+01:00';
"""

sql_deleteData="""

--
-- Delete data from the table 'ASTROSPHERE.VERMIETUNG_TELESKOP'
--
TRUNCATE TABLE ASTROSPHERE.VERMIETUNG_TELESKOP;

--
-- Delete data from the table 'ASTROSPHERE.VERMIETUNG_RAUM'
--
TRUNCATE TABLE ASTROSPHERE.VERMIETUNG_RAUM;

--
-- Delete data from the table 'ASTROSPHERE.VERKAUF_MERCH'
--
TRUNCATE TABLE ASTROSPHERE.VERKAUF_MERCH;

--
-- Delete data from the table 'ASTROSPHERE.VERKAUF_SNACK'
--
TRUNCATE TABLE ASTROSPHERE.VERKAUF_SNACK;

--
-- Delete data from the table 'ASTROSPHERE.VERANSTALTUNG_MEDIUM'
--
TRUNCATE TABLE ASTROSPHERE.VERANSTALTUNG_MEDIUM;

--
-- Delete data from the table 'ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER'
--
TRUNCATE TABLE ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER;

--
-- Delete data from the table 'ASTROSPHERE.BESTELLUNG'
--
TRUNCATE TABLE ASTROSPHERE.BESTELLUNG;

--
-- Delete data from the table 'ASTROSPHERE.VERANSTALTUNG'
--
DELETE FROM ASTROSPHERE.VERANSTALTUNG;

--
-- Delete data from the table 'ASTROSPHERE.MEDIUM'
--
DELETE FROM ASTROSPHERE.MEDIUM;

--
-- Delete data from the table 'ASTROSPHERE.VERKAUF'
--
DELETE FROM ASTROSPHERE.VERKAUF;

--
-- Delete data from the table 'ASTROSPHERE.STERN'
--
DELETE FROM ASTROSPHERE.STERN;

--
-- Delete data from the table 'ASTROSPHERE.PLANET'
--
DELETE FROM ASTROSPHERE.PLANET;

--
-- Delete data from the table 'ASTROSPHERE.RAUM'
--
DELETE FROM ASTROSPHERE.RAUM;

--
-- Delete data from the table 'ASTROSPHERE.PLANETENSYSTEM'
--
DELETE FROM ASTROSPHERE.PLANETENSYSTEM;

--
-- Delete data from the table 'ASTROSPHERE.KOMET'
--
DELETE FROM ASTROSPHERE.KOMET;

--
-- Delete data from the table 'ASTROSPHERE.NEBEL'
--
DELETE FROM ASTROSPHERE.NEBEL;

--
-- Delete data from the table 'ASTROSPHERE.ANGESTELLTER'
--
DELETE FROM ASTROSPHERE.ANGESTELLTER;

--
-- Delete data from the table 'ASTROSPHERE.TICKETSTUFE'
--
DELETE FROM ASTROSPHERE.TICKETSTUFE;

--
-- Delete data from the table 'ASTROSPHERE.TELESKOP'
--
DELETE FROM ASTROSPHERE.TELESKOP;

--
-- Delete data from the table 'ASTROSPHERE.STERNENBILD'
--
DELETE FROM ASTROSPHERE.STERNENBILD;

--
-- Delete data from the table 'ASTROSPHERE.SNACK'
--
DELETE FROM ASTROSPHERE.SNACK;

--
-- Delete data from the table 'ASTROSPHERE.MERCHARTIKEL'
--
DELETE FROM ASTROSPHERE.MERCHARTIKEL;

--
-- Delete data from the table 'ASTROSPHERE.LIEFERANT'
--
DELETE FROM ASTROSPHERE.LIEFERANT;

--
-- Delete data from the table 'ASTROSPHERE.KUNDE'
--
DELETE FROM ASTROSPHERE.KUNDE;

--
-- Delete data from the table 'ASTROSPHERE.GALAXIE'
--
DELETE FROM ASTROSPHERE.GALAXIE;

--
-- Delete data from the table 'ASTROSPHERE.ABTEILUNG'
--
DELETE FROM ASTROSPHERE.ABTEILUNG;

"""

sql_createData="""
--
-- Inserting data into table ASTROSPHERE.ABTEILUNG
--
INSERT INTO ASTROSPHERE.ABTEILUNG(NAME, BESCHREIBUNG) VALUES
('Verkauf', 'Die Abteilung Verkauf ist für den direkten Kundenkontakt und die Steigerung der Verkaufszahlen verantwortlich. Sie pflegt Beziehungen zu Kunden und arbeitet eng mit anderen Abteilungen zusammen, um die Bed rfnisse der Kunden zu erf llen.');
INSERT INTO ASTROSPHERE.ABTEILUNG(NAME, BESCHREIBUNG) VALUES
('Einkauf', 'Die Einkaufsabteilung ist verantwortlich für die Beschaffung von Waren, insbesondere für das Merchandise und die Lebensmittel, die in unserem Planetarium angeboten werden. Ihr Fokus liegt dabei auf der Auswahl qualitativ hochwertiger Produkte, effizienten Kostenverhandlungen mit Lieferanten und der Sicherstellung eines vielfältigen Angebots für unsere Besucher.');
INSERT INTO ASTROSPHERE.ABTEILUNG(NAME, BESCHREIBUNG) VALUES
('Marketing', 'Die Marketingabteilung entwickelt Marketingstrategien, um die Sichtbarkeit des Unternehmens zu erh hen, Produkte oder Dienstleistungen zu bewerben und potenzielle Kunden anzusprechen.');
INSERT INTO ASTROSPHERE.ABTEILUNG(NAME, BESCHREIBUNG) VALUES
('IT', 'Die IT-Abteilung k mmert sich um die Planung, Implementierung und Wartung von Informationstechnologien im Unternehmen, um eine reibungslose digitale Infrastruktur und Anwendungsunterst tzung zu gew hrleisten.');
INSERT INTO ASTROSPHERE.ABTEILUNG(NAME, BESCHREIBUNG) VALUES
('Veranstaltung', 'Die Veranstaltungsabteilung organisiert Veranstaltungen wie Vortr ge und Veranstaltungen für Kunden und Besucher. Zus tzlich laufen hier auch interne Veranstaltungen wie Mitarbeiterschulungen zusammen.');
INSERT INTO ASTROSPHERE.ABTEILUNG(NAME, BESCHREIBUNG) VALUES
('Sicherheit', 'Die Sicherheitsabteilung ist für die Gew hrleistung der physischen Sicherheit von Mitarbeitern, Verm genswerten und Einrichtungen verantwortlich, indem sie Sicherheitsrichtlinien und -ma nahmen implementiert.');
INSERT INTO ASTROSPHERE.ABTEILUNG(NAME, BESCHREIBUNG) VALUES
('Forschung', 'Die Forschungsabteilung widmet sich der Entdeckung neuer Inhalte für Veranstaltungen und wissenschaftlichen Arbeiten.');
INSERT INTO ASTROSPHERE.ABTEILUNG(NAME, BESCHREIBUNG) VALUES
('Vermietung', 'Die Vermietungsabteilung verwaltet VermietungsAktivitäten, sei es von R umlichkeiten oder Ausr stung, um zus tzliche Einnahmen zu generieren.');
INSERT INTO ASTROSPHERE.ABTEILUNG(NAME, BESCHREIBUNG) VALUES
('Personal', 'Die Personalabteilung k mmert sich um die Personalverwaltung, einschlie lich Einstellung, Schulung, Mitarbeiterentwicklung und die Umsetzung von Personalrichtlinien.');
INSERT INTO ASTROSPHERE.ABTEILUNG(NAME, BESCHREIBUNG) VALUES
('Finanzen', 'Die Finanzabteilung ist für die Buchf hrung, Budgetierung, Finanzberichterstattung und finanzielle Planung des Unternehmens zust ndig.');
INSERT INTO ASTROSPHERE.ABTEILUNG(NAME, BESCHREIBUNG) VALUES
('Design', 'Die Designabteilung konzentriert sich auf die kreative Gestaltung von Produkten, Grafiken oder anderen Elementen, um das  sthetische Erscheinungsbild des Unternehmens zu optimieren.');


--
-- Inserting data into table ASTROSPHERE.GALAXIE
--
INSERT INTO ASTROSPHERE.GALAXIE(NAME, DURCHMESSER_LJ, MASSE_KG, ENTFERNUNG_LJ, INFORMATIONEN) VALUES
('Milchstraße', 185000, 2.98365E39, 0, 'Die Milchstraße, auch Galaxis, ist die Galaxie, in der sich das Sonnensystem mit der Erde befindet. Entsprechend ihrer Form als flache Scheibe, die aus Hunderten von Milliarden Sternen besteht, ist die Milchstraße von der Erde aus als bandf rmige Aufhellung am Nachthimmel sichtbar, die sich über 360  erstreckt.');
INSERT INTO ASTROSPHERE.GALAXIE(NAME, DURCHMESSER_LJ, MASSE_KG, ENTFERNUNG_LJ, INFORMATIONEN) VALUES
('Andromeda', 2E6, 2.98365E47, 2.5E6, 'Die Andromedagalaxie, ist mit rund 2,5 Millionen Lichtjahren Entfernung die am nächsten zur Milchstraße gelegene Galaxie. Sie ist zugleich das entfernteste Objekt, das unter guten Bedingungen ohne technische Hilfsmittel mit blo em Auge beobachtet werden kann. Sie liegt im Sternbild Andromeda, von dem sie ihren Namen erbt. H ufig wird sie auch kurz als M31 bezeichnet nach ihrem Eintrag im Messier-Katalog.');


--
-- Inserting data into table ASTROSPHERE.KUNDE
--
INSERT INTO ASTROSPHERE.KUNDE(NAME, VORNAME, TELEFON_NR, EMAIL) VALUES
('Kruse', 'Hella', '+52 14 3932 7671', 'AbeSSims856@example.com');
INSERT INTO ASTROSPHERE.KUNDE(NAME, VORNAME, TELEFON_NR, EMAIL) VALUES
('Abert', 'Baldo ', '+52 41 2393 1767', 'Bolin641@example.com');
INSERT INTO ASTROSPHERE.KUNDE(NAME, VORNAME, TELEFON_NR, EMAIL) VALUES
('Hirsch', 'Tizian', '+33 3 18 95 10 73', 'Arroyo@nowhere.com');
INSERT INTO ASTROSPHERE.KUNDE(NAME, VORNAME, TELEFON_NR, EMAIL) VALUES
('Buchholz', 'Balduin ', '+44 299 816 3992', 'FrederickLandis@example.com');
INSERT INTO ASTROSPHERE.KUNDE(NAME, VORNAME, TELEFON_NR, EMAIL) VALUES
('Zurbriggen', 'Urban', '+44 4835 48 6840', 'Oralia_Sousa6@example.com');
INSERT INTO ASTROSPHERE.KUNDE(NAME, VORNAME, TELEFON_NR, EMAIL) VALUES
('Thaler', 'Cathrine', '+49-6577-702719', 'Bennett_J.Maldonado58@example.com');
INSERT INTO ASTROSPHERE.KUNDE(NAME, VORNAME, TELEFON_NR, EMAIL) VALUES
('Abich', 'Loritta', '+44 047 944 6714', 'AlesiaLilly47@nowhere.com');
INSERT INTO ASTROSPHERE.KUNDE(NAME, VORNAME, TELEFON_NR, EMAIL) VALUES
('Meissner', 'Edeltrude', '+49 (5710) 567804', 'lhonzjm1591@example.com');
INSERT INTO ASTROSPHERE.KUNDE(NAME, VORNAME, TELEFON_NR, EMAIL) VALUES
('Perl', 'Marlyse', '+380 25 651-332-9', 'AddisonS51@example.com');
INSERT INTO ASTROSPHERE.KUNDE(NAME, VORNAME, TELEFON_NR, EMAIL) VALUES
('Kaufmann', 'Emme', '+49 8078 486930', 'WillardAiello@nowhere.com');
INSERT INTO ASTROSPHERE.KUNDE(NAME, VORNAME, TELEFON_NR, EMAIL) VALUES
('Meltzer', 'Herlinde', '+49-0977-614490', 'qfaozsv350@example.com');
INSERT INTO ASTROSPHERE.KUNDE(NAME, VORNAME, TELEFON_NR, EMAIL) VALUES
('Schiller', 'Rabanus', '+32 5 361 55 95', 'EarnestAndres453@example.com');
INSERT INTO ASTROSPHERE.KUNDE(NAME, VORNAME, TELEFON_NR, EMAIL) VALUES
('Thalberg', 'Siw', '+44 2283 50 9733', 'xglzwedk.kovibhvvd@example.com');
INSERT INTO ASTROSPHERE.KUNDE(NAME, VORNAME, TELEFON_NR, EMAIL) VALUES
('Pfeifer', 'Farin', '+971 5 393 9090', 'DollyMares67@example.com');
INSERT INTO ASTROSPHERE.KUNDE(NAME, VORNAME, TELEFON_NR, EMAIL) VALUES
('Melzer', 'Uschi', '+44 179 003 6217', 'TiffanyM.Cunningham62@example.com');
INSERT INTO ASTROSPHERE.KUNDE(NAME, VORNAME, TELEFON_NR, EMAIL) VALUES
('Schirrmann', 'Xaver', '+55 41 7621-3168', 'Vernon_Estrada24@nowhere.com');
INSERT INTO ASTROSPHERE.KUNDE(NAME, VORNAME, TELEFON_NR, EMAIL) VALUES
('Gekkel', 'Eginhard', '+49 (5695) 405789', 'AdellAbreu@example.com');
INSERT INTO ASTROSPHERE.KUNDE(NAME, VORNAME, TELEFON_NR, EMAIL) VALUES
('Timroth', 'Gabriele', '+44 0145 989243', 'Peek26@nowhere.com');
INSERT INTO ASTROSPHERE.KUNDE(NAME, VORNAME, TELEFON_NR, EMAIL) VALUES
('Pfl ger', 'Hadassa', '+971 1 630 1009', 'Rubin432@example.com');
INSERT INTO ASTROSPHERE.KUNDE(NAME, VORNAME, TELEFON_NR, EMAIL) VALUES
('Schlechter', 'Mommo', '+44 423 640 6716', 'LalaHough@nowhere.com');
INSERT INTO ASTROSPHERE.KUNDE(NAME, VORNAME, TELEFON_NR, EMAIL) VALUES
('Buchloh', 'Arlett', '+49 (9720) 629876', 'dmeoo8@nowhere.com');
INSERT INTO ASTROSPHERE.KUNDE(NAME, VORNAME, TELEFON_NR, EMAIL) VALUES
('Abicht', 'Ottokar', '+380 80 755-192-4', 'Hammett@example.com');
INSERT INTO ASTROSPHERE.KUNDE(NAME, VORNAME, TELEFON_NR, EMAIL) VALUES
('K chelbecker', 'Dianara', '+52 07 7638 5917', 'YeseniaMyers536@nowhere.com');
INSERT INTO ASTROSPHERE.KUNDE(NAME, VORNAME, TELEFON_NR, EMAIL) VALUES
('Hirschmann', 'Lisiane', '+971 9 691 6739', 'Stack837@nowhere.com');
INSERT INTO ASTROSPHERE.KUNDE(NAME, VORNAME, TELEFON_NR, EMAIL) VALUES
('Kaulbach', 'Bernfried', '+55 17 1097-6574', 'Alston13@nowhere.com');


--
-- Inserting data into table ASTROSPHERE.LIEFERANT
--
INSERT INTO ASTROSPHERE.LIEFERANT(NAME) VALUES
('Coca Cola');
INSERT INTO ASTROSPHERE.LIEFERANT(NAME) VALUES
('Super Pop Inc.');
INSERT INTO ASTROSPHERE.LIEFERANT(NAME) VALUES
('Elemental Electronics');
INSERT INTO ASTROSPHERE.LIEFERANT(NAME) VALUES
('Pen and Jerrys Paper Inc.');
INSERT INTO ASTROSPHERE.LIEFERANT(NAME) VALUES
('Promohub');
INSERT INTO ASTROSPHERE.LIEFERANT(NAME) VALUES
('Worldwide wearables');
INSERT INTO ASTROSPHERE.LIEFERANT(NAME) VALUES
('Snackaria Gmbh');
INSERT INTO ASTROSPHERE.LIEFERANT(NAME) VALUES
('Greener Food');
INSERT INTO ASTROSPHERE.LIEFERANT(NAME) VALUES
('Frying Friends');
INSERT INTO ASTROSPHERE.LIEFERANT(NAME) VALUES
('Muenchner Moenchsbrauerei');


--
-- Inserting data into table ASTROSPHERE.MERCHARTIKEL
--
INSERT INTO ASTROSPHERE.MERCHARTIKEL(BEZEICHNUNG, BESCHREIBUNG, GROESSE, VERKAUF_PREIS_STK, IMAGE_PATH) VALUES
('AstroHoodie', 'Bequemer und stylischer Hoodie aus weicher Baumwollmischung mit Kängurutasche und verstellbarer Kapuze. Ideal für jeden Tag.', 'S', 69.99, '../static/images/products/AstroHoodie.png');
INSERT INTO ASTROSPHERE.MERCHARTIKEL(BEZEICHNUNG, BESCHREIBUNG, GROESSE, VERKAUF_PREIS_STK, IMAGE_PATH) VALUES
('AstroHoodie', 'Bequemer und stylischer Hoodie aus weicher Baumwollmischung mit Kängurutasche und verstellbarer Kapuze. Ideal für jeden Tag.', 'M', 69.99, '../static/images/products/AstroHoodie.png');
INSERT INTO ASTROSPHERE.MERCHARTIKEL(BEZEICHNUNG, BESCHREIBUNG, GROESSE, VERKAUF_PREIS_STK, IMAGE_PATH) VALUES
('AstroHoodie', 'Bequemer und stylischer Hoodie aus weicher Baumwollmischung mit Kängurutasche und verstellbarer Kapuze. Ideal für jeden Tag.', 'L', 69.99, '../static/images/products/AstroHoodie.png');
INSERT INTO ASTROSPHERE.MERCHARTIKEL(BEZEICHNUNG, BESCHREIBUNG, GROESSE, VERKAUF_PREIS_STK, IMAGE_PATH) VALUES
('AstroShirt', 'Klassisches, bequemes T-Shirt aus hochwertiger Baumwolle, ideal für jeden Tag.', 'S', 19.99, '../static/images/products/AstroShirt.png');
INSERT INTO ASTROSPHERE.MERCHARTIKEL(BEZEICHNUNG, BESCHREIBUNG, GROESSE, VERKAUF_PREIS_STK, IMAGE_PATH) VALUES
('AstroShirt', 'Klassisches, bequemes T-Shirt aus hochwertiger Baumwolle, ideal für jeden Tag.', 'M', 19.99, '../static/images/products/AstroShirt.png');
INSERT INTO ASTROSPHERE.MERCHARTIKEL(BEZEICHNUNG, BESCHREIBUNG, GROESSE, VERKAUF_PREIS_STK, IMAGE_PATH) VALUES
('AstroShirt', 'Klassisches, bequemes T-Shirt aus hochwertiger Baumwolle, ideal für jeden Tag.', 'L', 19.99, '../static/images/products/AstroShirt.png');
INSERT INTO ASTROSPHERE.MERCHARTIKEL(BEZEICHNUNG, BESCHREIBUNG, GROESSE, VERKAUF_PREIS_STK, IMAGE_PATH) VALUES
('Solar System Socks', 'Weiche, strapazierfähige Socken aus Baumwollmischung für den täglichen Gebrauch', NULL, 18.99, '../static/images/products/SolarSystem_Socks.png');
INSERT INTO ASTROSPHERE.MERCHARTIKEL(BEZEICHNUNG, BESCHREIBUNG, GROESSE, VERKAUF_PREIS_STK, IMAGE_PATH) VALUES
('Marsian Mug', 'Robuste Keramiktasse mit glänzender Oberfläche und großem Fassungsvermögen, perfekt für heiße Getränke.', NULL, 9.99, '../static/images/products/Marsian_Mug.png');
INSERT INTO ASTROSPHERE.MERCHARTIKEL(BEZEICHNUNG, BESCHREIBUNG, GROESSE, VERKAUF_PREIS_STK, IMAGE_PATH) VALUES
('Milkyway Mug', 'Robuste Keramiktasse mit glänzender Oberfläche und großem Fassungsvermögen, perfekt für heiße Getränke.',NULL, 9.99, '../static/images/products/Milkyway_Mug.png');
INSERT INTO ASTROSPHERE.MERCHARTIKEL(BEZEICHNUNG, BESCHREIBUNG, GROESSE, VERKAUF_PREIS_STK, IMAGE_PATH) VALUES
('Uranus USB Stick', 'Hochwertiger USB-Stick mit schneller Datenübertragung und robustem Gehäuse',NULL, 14.99, '../static/images/products/Uranus_USB_Stick.png');
INSERT INTO ASTROSPHERE.MERCHARTIKEL(BEZEICHNUNG, BESCHREIBUNG, GROESSE, VERKAUF_PREIS_STK, IMAGE_PATH) VALUES
('Venus Vase', 'Elegante Glasvase mit schlankem Design, perfekt für Blumenarrangements und als dekoratives Element in jedem Raum.',NULL, 59.99, '../static/images/products/Venus_Vase.png');
INSERT INTO ASTROSPHERE.MERCHARTIKEL(BEZEICHNUNG, BESCHREIBUNG, GROESSE, VERKAUF_PREIS_STK, IMAGE_PATH) VALUES
('Jupiter Journal', 'Stilvolles Journal mit robustem Einband, ideal für Notizen, Skizzen und persönliche Aufzeichnungen unterwegs.',NULL, 7.99, '../static/images/products/Jupiter_Journal.png');
INSERT INTO ASTROSPHERE.MERCHARTIKEL(BEZEICHNUNG, BESCHREIBUNG, GROESSE, VERKAUF_PREIS_STK, IMAGE_PATH) VALUES
('Neptune Notebook', 'Praktisches Notizbuch mit strapazierfähigem Einband, perfekt für Mitschriften, Skizzen und unterwegs.',NULL, 9.99, '../static/images/products/Neptune_Notebook.png');
INSERT INTO ASTROSPHERE.MERCHARTIKEL(BEZEICHNUNG, BESCHREIBUNG, GROESSE, VERKAUF_PREIS_STK, IMAGE_PATH) VALUES
('Meteor Magnet', 'Robuster Magnet mit ansprechendem Design, ideal für den Kühlschrank oder als dekoratives Element.',NULL, 5.99, '../static/images/products/Meteor_Magnet.png');
INSERT INTO ASTROSPHERE.MERCHARTIKEL(BEZEICHNUNG, BESCHREIBUNG, GROESSE, VERKAUF_PREIS_STK, IMAGE_PATH) VALUES
('Saturn Sunglasses', 'Modische Sonnenbrille mit UV-Schutzgläsern, die perfekt für sonnige Tage und einen coolen Look geeignet ist.',NULL, 14.99, '../static/images/products/Saturn_Sunglasses.png');
INSERT INTO ASTROSPHERE.MERCHARTIKEL(BEZEICHNUNG, BESCHREIBUNG, GROESSE, VERKAUF_PREIS_STK, IMAGE_PATH) VALUES
('Venus Vest', 'Stylische Weste aus hochwertigem Material, ideal für Layering und einen modernen Look.','S', 49.99, '../static/images/products/Venus_Vest.png');
INSERT INTO ASTROSPHERE.MERCHARTIKEL(BEZEICHNUNG, BESCHREIBUNG, GROESSE, VERKAUF_PREIS_STK, IMAGE_PATH) VALUES
('Venus Vest', 'Stylische Weste aus hochwertigem Material, ideal für Layering und einen modernen Look.','M', 49.99, '../static/images/products/Venus_Vest.png');
INSERT INTO ASTROSPHERE.MERCHARTIKEL(BEZEICHNUNG, BESCHREIBUNG, GROESSE, VERKAUF_PREIS_STK, IMAGE_PATH) VALUES
('Venus Vest', 'Stylische Weste aus hochwertigem Material, ideal für Layering und einen modernen Look.','L', 49.99, '../static/images/products/Venus_Vest.png');
INSERT INTO ASTROSPHERE.MERCHARTIKEL(BEZEICHNUNG, BESCHREIBUNG, GROESSE, VERKAUF_PREIS_STK, IMAGE_PATH) VALUES
('Nebula Napkins', 'Hochwertiges Serviettenset aus Baumwolle, perfekt für besondere Anlässe und den täglichen Gebrauch.',NULL, 4.99, '../static/images/products/Nebula_Napkins.png');
INSERT INTO ASTROSPHERE.MERCHARTIKEL(BEZEICHNUNG, BESCHREIBUNG, GROESSE, VERKAUF_PREIS_STK, IMAGE_PATH) VALUES
('Uranus Umbrella', 'Robuster Regenschirm mit automatischem Öffnungsmechanismus, ideal für regnerische Tage und unterwegs.','L', 15.99, '../static/images/products/Uranus_Umbrella.png');


--
-- Inserting data into table ASTROSPHERE.SNACK
--
INSERT INTO ASTROSPHERE.SNACK(BEZEICHNUNG, BESCHREIBUNG, VERKAUF_PREIS_STK, GROESSE, IMAGE_PATH) VALUES
('Neptune Nachos', 'Knackige Maischips mit würziger Käsesauce, perfekt für Snacks oder als Beilage zu Dips.', 3.99, 'M', '../static/images/snacks/Neptune_Nachos.png');
INSERT INTO ASTROSPHERE.SNACK(BEZEICHNUNG, BESCHREIBUNG, VERKAUF_PREIS_STK, GROESSE, IMAGE_PATH) VALUES
('Neptune Nachos', 'Knackige Maischips mit würziger Käsesauce, perfekt für Snacks oder als Beilage zu Dips.', 4.99, 'L', '../static/images/snacks/Neptune_Nachos.png');
INSERT INTO ASTROSPHERE.SNACK(BEZEICHNUNG, BESCHREIBUNG, VERKAUF_PREIS_STK, GROESSE, IMAGE_PATH) VALUES
('Planetary Popcorn Salt', 'Luftig-leichtes Popcorn mit einer perfekten Balance aus Knusprigkeit und salzigem Geschmack.', 2.49, 'M', '../static/images/snacks/Planetary_Popcorn_Salt.png');
INSERT INTO ASTROSPHERE.SNACK(BEZEICHNUNG, BESCHREIBUNG, VERKAUF_PREIS_STK, GROESSE, IMAGE_PATH) VALUES
('Planetary Popcorn Salt', 'Luftig-leichtes Popcorn mit einer perfekten Balance aus Knusprigkeit und salzigem Geschmack.', 3.49, 'L' ,'../static/images/snacks/Planetary_Popcorn_Salt.png');
INSERT INTO ASTROSPHERE.SNACK(BEZEICHNUNG, BESCHREIBUNG, VERKAUF_PREIS_STK, GROESSE, IMAGE_PATH) VALUES
('Planetary Popcorn Sugar', 'Luftig-leichtes Popcorn mit einer köstlichen Zuckerglasur.', 2.49, 'M', '../static/images/snacks/Planetary_Popcorn_Sugar.png');
INSERT INTO ASTROSPHERE.SNACK(BEZEICHNUNG, BESCHREIBUNG, VERKAUF_PREIS_STK, GROESSE, IMAGE_PATH) VALUES
('Planetary Popcorn Sugar', 'Luftig-leichtes Popcorn mit einer köstlichen Zuckerglasur.', 3.49, 'L', '../static/images/snacks/Planetary_Popcorn_Sugar.png');
INSERT INTO ASTROSPHERE.SNACK(BEZEICHNUNG, BESCHREIBUNG, VERKAUF_PREIS_STK, GROESSE, IMAGE_PATH) VALUES
('Solary Salad', 'Knackiger Salat mit einer bunten Mischung aus frischen Gemüsesorten und einem leicht würzigen Dressing.', 5.99, 'M', '../static/images/snacks/Solary_Salad.png');
INSERT INTO ASTROSPHERE.SNACK(BEZEICHNUNG, BESCHREIBUNG, VERKAUF_PREIS_STK, GROESSE, IMAGE_PATH) VALUES
('Venus Vinegar Chips', 'Knackige Kartoffelchips mit einem würzigen Essiggeschmack, perfekt für Liebhaber von herzhaften Snacks.', 1.99, 'M', '../static/images/snacks/Venus_Vinegar_Chips.png');
INSERT INTO ASTROSPHERE.SNACK(BEZEICHNUNG, BESCHREIBUNG, VERKAUF_PREIS_STK, GROESSE, IMAGE_PATH) VALUES
('Zodiac Sourcreme Chips', 'Knackige Kartoffelchips mit einem cremigen Sauerrahmgeschmack und einer leichten Würze, ideal für Snackliebhaber.', 1.99, 'M', '../static/images/snacks/Zodiac_Sourcreme_Chips.png');
INSERT INTO ASTROSPHERE.SNACK(BEZEICHNUNG, BESCHREIBUNG, VERKAUF_PREIS_STK, GROESSE, IMAGE_PATH) VALUES
('Galaxie Gummi Bears', 'Fruchtige und weiche Gummibären in verschiedenen Geschmacksrichtungen, ein beliebter Snack für Jung und Alt.', 1.49, 'M', '../static/images/snacks/Galaxie_Gummi_Bears.png');
INSERT INTO ASTROSPHERE.SNACK(BEZEICHNUNG, BESCHREIBUNG, VERKAUF_PREIS_STK, GROESSE, IMAGE_PATH) VALUES
('Cosmic Coke', 'Kohlensäurehaltiges Erfrischungsgetränk mit einem unverwechselbaren Geschmack.', 1.99, 'M', '../static/images/snacks/Cosmic_Coke.png');
INSERT INTO ASTROSPHERE.SNACK(BEZEICHNUNG, BESCHREIBUNG, VERKAUF_PREIS_STK, GROESSE, IMAGE_PATH) VALUES
('Cosmic Coke', 'Kohlensäurehaltiges Erfrischungsgetränk mit einem unverwechselbaren Geschmack.', 2.49, 'L', '../static/images/snacks/Cosmic_Coke.png');
INSERT INTO ASTROSPHERE.SNACK(BEZEICHNUNG, BESCHREIBUNG, VERKAUF_PREIS_STK, GROESSE, IMAGE_PATH) VALUES
('Cosmic Coke Zero', 'Kohlensäurehaltiges Erfrischungsgetränk ohne Zucker, aber mit dem vollen Geschmack von Cola.', 2.09, 'M', '../static/images/snacks/Cosmic_Coke_Zero.png');
INSERT INTO ASTROSPHERE.SNACK(BEZEICHNUNG, BESCHREIBUNG, VERKAUF_PREIS_STK, GROESSE, IMAGE_PATH) VALUES
('Cosmic Coke Zero', 'Kohlensäurehaltiges Erfrischungsgetränk ohne Zucker, aber mit dem vollen Geschmack von Cola.', 2.59, 'L', '../static/images/snacks/Cosmic_Coke_Zero.png');
INSERT INTO ASTROSPHERE.SNACK(BEZEICHNUNG, BESCHREIBUNG, VERKAUF_PREIS_STK, GROESSE, IMAGE_PATH) VALUES
('Space Sprite', 'Kohlensäurehaltiges Erfrischungsgetränk mit einem zitronigen Geschmack und einer leichten Süße.', 1.99, 'M', '../static/images/snacks/Space_Sprite.png');
INSERT INTO ASTROSPHERE.SNACK(BEZEICHNUNG, BESCHREIBUNG, VERKAUF_PREIS_STK, GROESSE, IMAGE_PATH) VALUES
('Space Sprite', 'Kohlensäurehaltiges Erfrischungsgetränk mit einem zitronigen Geschmack und einer leichten Süße.', 2.49, 'L', '../static/images/snacks/Space_Sprite.png');
INSERT INTO ASTROSPHERE.SNACK(BEZEICHNUNG, BESCHREIBUNG, VERKAUF_PREIS_STK, GROESSE, IMAGE_PATH) VALUES
('Space Sprite Zero', 'Kohlensäurehaltiges Erfrischungsgetränk mit einem zitronigen Geschmack, aber ohne Zucker.', 2.09, 'M', '../static/images/snacks/Space_Sprite_Zero.png');
INSERT INTO ASTROSPHERE.SNACK(BEZEICHNUNG, BESCHREIBUNG, VERKAUF_PREIS_STK, GROESSE, IMAGE_PATH) VALUES
('Space Sprite Zero', 'Kohlensäurehaltiges Erfrischungsgetränk mit einem zitronigen Geschmack, aber ohne Zucker.', 2.59, 'L', '../static/images/snacks/Space_Sprite_Zero.png');
INSERT INTO ASTROSPHERE.SNACK(BEZEICHNUNG, BESCHREIBUNG, VERKAUF_PREIS_STK, GROESSE, IMAGE_PATH) VALUES
('Interplanetary IceTea', 'Kühlender Eistee mit einem Hauch von Zitrone und einer leichten Süße, perfekt für heiße Tage.', 2.99, 'M', '../static/images/snacks/Interplanetary_IceTea.png');
INSERT INTO ASTROSPHERE.SNACK(BEZEICHNUNG, BESCHREIBUNG, VERKAUF_PREIS_STK, GROESSE, IMAGE_PATH) VALUES
('Interplanetary IceTea', 'Kühlender Eistee mit einem Hauch von Zitrone und einer leichten Süße, perfekt für heiße Tage.', 3.49, 'L', '../static/images/snacks/Interplanetary_IceTea.png');
INSERT INTO ASTROSPHERE.SNACK(BEZEICHNUNG, BESCHREIBUNG, VERKAUF_PREIS_STK, GROESSE, IMAGE_PATH) VALUES
('Interplanetary IceTea Zero', 'Kühlender Eistee mit einem Hauch von Zitrone und keinerlei Zucker.', 3.09, 'M', '../static/images/snacks/Interplanetary_IceTea_Zero.png');
INSERT INTO ASTROSPHERE.SNACK(BEZEICHNUNG, BESCHREIBUNG, VERKAUF_PREIS_STK, GROESSE, IMAGE_PATH) VALUES
('Interplanetary IceTea Zero', 'Kühlender Eistee mit einem Hauch von Zitrone und keinerlei Zucker.', 3.59, 'L', '../static/images/snacks/Interplanetary_IceTea_Zero.png');
INSERT INTO ASTROSPHERE.SNACK(BEZEICHNUNG, BESCHREIBUNG, VERKAUF_PREIS_STK, GROESSE, IMAGE_PATH) VALUES
('Big Bang Beer', 'Hopfenhaltiges Getränk mit einem angenehmen Bittergeschmack und malzigen Aromen.', 4.99, 'M', '../static/images/snacks/Big_Bang_Beer.png');
INSERT INTO ASTROSPHERE.SNACK(BEZEICHNUNG, BESCHREIBUNG, VERKAUF_PREIS_STK, GROESSE, IMAGE_PATH) VALUES
('Big Bang Beer', 'Hopfenhaltiges Getränk mit einem angenehmen Bittergeschmack und malzigen Aromen.', 5.99, 'L', '../static/images/snacks/Big_Bang_Beer.png');
INSERT INTO ASTROSPHERE.SNACK(BEZEICHNUNG, BESCHREIBUNG, VERKAUF_PREIS_STK, GROESSE, IMAGE_PATH) VALUES
('Parsec Peanuts', 'Geröstete Erdnüsse mit einer leichten Salznote, ideal als Snack für zwischendurch.', 1.49, 'M', '../static/images/snacks/Parsec_Peanuts.png');


--
-- Inserting data into table ASTROSPHERE.STERNENBILD
--
INSERT INTO ASTROSPHERE.STERNENBILD(NAME, ANZAHL_STERNE, INFORMATIONEN) VALUES
('Steinbock', 10, 'Der Steinbock (auch Ziegenfisch, deshalb oft mit Fischschwanz dargestellt) ist ein unscheinbares Sternbild zwischen dem Wassermann und dem Sch tzen.');
INSERT INTO ASTROSPHERE.STERNENBILD(NAME, ANZAHL_STERNE, INFORMATIONEN) VALUES
('Wassermann', 15, 'Der Wassermann ist ein ausgedehntes, aber wenig auff lliges Sternbild des herbstlichen Sternenhimmels, das sich s dlich des Pegasus befindet.');
INSERT INTO ASTROSPHERE.STERNENBILD(NAME, ANZAHL_STERNE, INFORMATIONEN) VALUES
('Fische', 20, 'Die Fische liegen auf der Ekliptik, daher ziehen Sonne, Mond und die Planeten durch das Sternbild.');
INSERT INTO ASTROSPHERE.STERNENBILD(NAME, ANZAHL_STERNE, INFORMATIONEN) VALUES
('Widder', 4, 'Der Widder ist ein kleines, doch markantes Sternbild. Er liegt s dlich des unauff lligen Sternbildes Dreieck und  stlich der Fische.');
INSERT INTO ASTROSPHERE.STERNENBILD(NAME, ANZAHL_STERNE, INFORMATIONEN) VALUES
('Stier', 11, 'Der Stier ist ein Sternbild n rdlich des Orion. Es liegt beidseits der Ekliptik.');
INSERT INTO ASTROSPHERE.STERNENBILD(NAME, ANZAHL_STERNE, INFORMATIONEN) VALUES
('Zwillinge', 17, 'Die Zwillinge bilden ein lang gezogenes Rechteck. Die auff llig hellen Sterne Castor und Pollux bilden die beiden nord stlichen Eckpunkte. Durch den westlichen Teil der Zwillinge zieht sich das Band der Milchstraße, daher findet man in diesem Bereich mehrere offene Sternhaufen.');
INSERT INTO ASTROSPHERE.STERNENBILD(NAME, ANZAHL_STERNE, INFORMATIONEN) VALUES
('Krebs', 6, 'Der Krebs ist ein unauff lliges Sternbild, das aus relativ lichtschwachen Sternen gebildet wird. Das Sternbild ist daher etwas schwierig zu entdecken. Am besten findet man es, indem man einer gedachten Linie zwischen den markanten Sternbildern Zwillinge und L we folgt. Die Sterne des Krebses formen ein auf dem Kopf stehendes Y.');
INSERT INTO ASTROSPHERE.STERNENBILD(NAME, ANZAHL_STERNE, INFORMATIONEN) VALUES
('L we', 9, 'Der L we ist ein markantes Sternbild, das am Fr hjahrshimmel leicht erkennbar ist. Aufgrund der Form einer gebogene Linie von Sternen wird mitunter auch als  Sichel  bezeichnet.');
INSERT INTO ASTROSPHERE.STERNENBILD(NAME, ANZAHL_STERNE, INFORMATIONEN) VALUES
('Jungfrau', 12, 'Die Jungfrau ist (nach der Wasserschlange) das zweitgrößte Sternbild am Himmel. Sie liegt zwischen dem L wen und der Waage. Die hellsten Sterne sollen eine liegende Person darstellen.');
INSERT INTO ASTROSPHERE.STERNENBILD(NAME, ANZAHL_STERNE, INFORMATIONEN) VALUES
('Waage', 4, 'Die Waage ist ein Sternbild zwischen dem Skorpion und der Jungfrau. Die Waage liegt auf der Ekliptik, so dass Sonne, Mond und die Planeten durch sie hindurch ziehen.');
INSERT INTO ASTROSPHERE.STERNENBILD(NAME, ANZAHL_STERNE, INFORMATIONEN) VALUES
('Skorpion', 14, 'Der Skorpion ist ein imposantes Sternbild am Südhimmel. Eine gewundene, helle Sternenkette bildet den bekannten Asterismus, der die Gestalt eines Skorpions mit Scheren und aufgerichtetem Stachel erkennen lüsst. Aufgrund seiner s dlichen Lage ist das Sternbild von Mitteleuropa aus nur im Sommer, knapp am S dhorizont zu finden. Es liegt in der N he des Zentrums der Milchstraße und enth lt daher eine Vielzahl an Sternhaufen und Nebeln.');
INSERT INTO ASTROSPHERE.STERNENBILD(NAME, ANZAHL_STERNE, INFORMATIONEN) VALUES
('Schlangenträger', 8, 'Der Schlangenträger ist ein sehr ausgedehntes, aber wenig auff lliges Sternbild am Sommerhimmel der Nordhalbkugel. Da seine Sterne weit auseinandergezogen und wenig markant sind, ist es nicht ganz einfach, ihn zwischen dem Herkules und dem Skorpion zu identifizieren. Der Schlangenträger besitzt eine ringf rmige Gestalt, von der westlich und  stlich die Sterne der Schlange ausgehen. Durch den westlichen Teil zieht sich das Band der Milchstraße.');
INSERT INTO ASTROSPHERE.STERNENBILD(NAME, ANZAHL_STERNE, INFORMATIONEN) VALUES
('Sch tze', 15, 'Der Sch tze ist das s dlichste Tierkreis-Sternbild, er liegt zwischen dem Skorpion und dem Steinbock. Die hellsten Sterne des Sch tzen bilden eine Form, die an einen Teekessel erinnert. Im englischen Sprachraum wird er daher h ufig als  Teapot  bezeichnet. Der Sch tze liegt in den sternenreichsten Bereichen der Milchstraße; in dieser Richtung befindet sich das galaktische Zentrum.');
INSERT INTO ASTROSPHERE.STERNENBILD(NAME, ANZAHL_STERNE, INFORMATIONEN) VALUES
('Zentaur', 17, 'Der Zentaur ist ein gro es, sehr auff lliges Sternbild des Südhimmels. Es stellt den weisen Cheiron der griechischen Mythologie dar, den Lehrer von Achill und  skulap. Der Zentaur ist ein ausgedehntes Sternbild, das sich s dlich der Wasserschlange erstreckt.');


--
-- Inserting data into table ASTROSPHERE.TELESKOP
--
INSERT INTO ASTROSPHERE.TELESKOP(BEZEICHNUNG, TYP, TAGES_MIET_PREIS, BESCHREIBUNG) VALUES
('E-ELT European Extremely Large Telescope', 'Spiegelteleskop', 150.00, 'Als Teil des European Southern Observatory (ESO) befindet sich das European Extremely Large Telescope, kurz E-ELT, ebenfalls in Chile. Das Spiegelteleskop befindet sich seit 2017 im Bau und soll mit einem Durchmesser von 39 Metern das bisher groesste Spiegel- sowie Nahinfrarot-Teleskop werden. Dadurch ist es laut ESO moeglich, etwa 13 Mal mehr Licht einzufangen als die groessten optischen Instrumente in der Gegenwart');
INSERT INTO ASTROSPHERE.TELESKOP(BEZEICHNUNG, TYP, TAGES_MIET_PREIS, BESCHREIBUNG) VALUES
('SOFIA Stratosphaeren-Observatorium fuer Infrarot-Astronomie', 'Infrarotteleskop', 185.00, 'Die Kombination aus 2,5-Meter-Teleskop und Boeing 747SP (die kurze Langstrecken-Version) erreicht zwar nicht die Aufloesung vieler bodengestuetzter Systeme, eroeffnet aber Projekte, welche vom Boden aus nicht moeglich waeren. Dabei handelt es sich zum Beispiel um die Beobachtung von Infrarot-Wellenlaengen');
INSERT INTO ASTROSPHERE.TELESKOP(BEZEICHNUNG, TYP, TAGES_MIET_PREIS, BESCHREIBUNG) VALUES
('FAST Five Hundred Meter Aperture Spherical Telescope', 'Radioteleskop', 230.00, 'Das weltweit groesste Einzel-Radioteleskop weist einen Hauptspiegeldurchmesser von rund 520 Metern auf. Eine an Seilen befestigte und manoevrierbare Fokuskabine bietet zudem einen veraenderbaren Parabolspiegelbereich mit einem Durchmesser von 300 Metern und soll die Aufloesung der empfangenen Signale erhoehen');
INSERT INTO ASTROSPHERE.TELESKOP(BEZEICHNUNG, TYP, TAGES_MIET_PREIS, BESCHREIBUNG) VALUES
('LZT Large Zenith Telescope', 'Fluessigspiegelteleskop', NULL, 'Mit nur sechs Metern Spiegeldurchmesser zaehlt das Large Zenith Telescope auf rund 400 Metern ueber dem Meeresspiegel im kanadischen Malcolm Knapp Research Forest zwar nicht zu den groessten Teleskopen ueberhaupt. Im Bereich der Zenit-Teleskope ist es mit einem Gewicht von rund drei Tonnen das weltweit Groesste');
INSERT INTO ASTROSPHERE.TELESKOP(BEZEICHNUNG, TYP, TAGES_MIET_PREIS, BESCHREIBUNG) VALUES
('EHT Event Horizon Telescope', 'Radioteleskop', 270.00, 'Ein besonderer Vertreter der Interferometrie (Very Long Baseline Interferometry, VLBI) nutzt einen Verbund aus Radioteleskopen, um schwarze Loecher zu untersuchen. Die einzelnen Antennen des Event Horizon Telescope (EHT) befinden sich ueber den gesamten Globus verteilt, um dadurch eine moeglichst grosse Winkelaufloesung zu erhalten. Die Genauigkeit liegt hier bei einem Vielfachen eines konventionellen Radioteleskops');


--
-- Inserting data into table ASTROSPHERE.TICKETSTUFE
--
INSERT INTO ASTROSPHERE.TICKETSTUFE(STUFE, ZEITRAUM, PREIS, IMAGE_PATH) VALUES
('Tag', 1, 25.00, '../static/images/tickets/tagesticket.png');
INSERT INTO ASTROSPHERE.TICKETSTUFE(STUFE, ZEITRAUM, PREIS, IMAGE_PATH) VALUES
('Monat', 30, 75.00, '../static/images/tickets/monatsticket.png');
INSERT INTO ASTROSPHERE.TICKETSTUFE(STUFE, ZEITRAUM, PREIS, IMAGE_PATH) VALUES
('Jahr', 365, 110.00, '../static/images/tickets/jahresticket.png');


--
-- Inserting data into table ASTROSPHERE.ANGESTELLTER
--
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(NULL, 4, 'Kleiner', 'Paschalis', 5126.56);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(1, 10, 'Leist', 'Joerge', 3069.86);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(1, 1, 'Kleinermann', 'Felin', 3013.03);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(1, 8, 'Paulig', 'Balintt ', 5402.6);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(1, 4, 'Zurbriggen', 'Filiberta', 4457.12);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(1, 4, 'Forster', 'Filina', 5429.74);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(1, 3, 'Schlechter', 'Gotfrit', 2471.51);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(1, 9, 'Tischbein', 'Adelisa ', 3151.59);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(1, 2, 'Heitsch', 'Cathrine', 2459.32);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(1, 10, 'Abicht', 'Basileo ', 5247.51);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(1, 8, 'Franke', 'Elika', 3399.43);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(2, 4, 'Meier', 'Volkbert', 4446.9);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(3, 1, 'Schmidt', 'Waldomir', 3005.52);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(4, 7, 'Leitner', 'Burkhard', 5787.17);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(5, 9, 'Kleinmann', 'Jule', 3955.94);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(5, 3, 'Heldman', 'Santian', 2475.88);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(6, 6, 'Franz', 'Aloysia', 2931.93);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(2, 8, 'Henkel', 'Detmar', 3453.66);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(3, 3, 'Tischler', 'Lowis', 3645.96);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(3, 3, 'Peiper', 'Tius', 3159.57);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(4, 8, 'Meissner', 'J rg', 4648.37);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(7, 2, 'Schmitz', 'Danja', 4341.74);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(7, 6, 'Tissen', 'Eckhart', 2850.99);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(9, 7, 'Buchmeyer', 'Deborian', 3636.45);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(8, 3, 'Adler', 'D rtlis', 5558.98);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(9, 6, 'Buchner', 'Eligius', 4791.42);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(11, 1, 'Schneider', 'Fritz', 5118.16);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(11, 7, 'Totleben', 'Konradin', 3114.91);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(11, 7, 'Albrecht', 'Caruso', 2674.89);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(10, 2, 'Perl', 'Selinda', 2257.86);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(10, 5, 'Meltzer', 'Teoresa', 4580.75);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(5, 10, 'Schneidermann', 'Cornell', 4717.73);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(8, 3, 'Treviranus', 'Miria', 5136.61);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(2, 5, 'Scholl', 'Skyla', 5656.05);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(5, 4, 'Lemm', 'B rbel', 3533.38);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(9, 6, 'B chner', 'Helmute', 5743.36);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(10, 9, 'Altmann', 'Eustachius', 3819.31);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(8, 9, 'Tr bner', 'Thees', 3833.11);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(7, 8, 'Kleist', 'Edelgard', 4736.6);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(2, 6, 'Lengefeld', 'Role', 4208.31);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(3, 8, 'Klemperer', 'Lusia', 3447.84);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(4, 7, 'Sch n', 'Annafee', 2050.44);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(5, 3, 'Lenz', 'Jolena', 4057.05);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(8, 10, 'Klenze', 'Sonja', 3809.26);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(9, 5, 'Frenzel', 'Suso', 4584.01);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(11, 8, 'Lerch', 'Dorit', 2599.26);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(8, 9, 'Ude', 'Waldefried', 5922.27);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(9, 1, 'Klinger', 'Kresandra', 5048);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(10, 7, 'Pfeifer', 'R der', 3890.54);
INSERT INTO ASTROSPHERE.ANGESTELLTER(CHEF_ID, ABTEILUNG_ID, NAME, VORNAME, GEHALT) VALUES
(4, 2, 'Melzer', 'Eyck', 2281.82);


--
-- Inserting data into table ASTROSPHERE.NEBEL
--
INSERT INTO ASTROSPHERE.NEBEL(GALAXIE_ID, NAME, DURCHMESSER_LJ, MASSE_KG, ENTFERNUNG_LJ, INFORMATIONEN) VALUES
(1, 'Ringnebel', 0.9, 3.9782E29, 2300, 'Der Ringnebel ist ein Planetarischer Nebel im Sternbild Leier. Der Nebel ist der überrest eines Sterns, der vor etwa 20.000 Jahren seine äußere Gash lle abgesto en hat. ');
INSERT INTO ASTROSPHERE.NEBEL(GALAXIE_ID, NAME, DURCHMESSER_LJ, MASSE_KG, ENTFERNUNG_LJ, INFORMATIONEN) VALUES
(1, 'S dlicher Ringnebel', 0.5, NULL, 2000, 'Der S dlicher Ringnebel, benannt aufgrund seiner  hnlichkeit zum Ringnebel, ist ein Planetarischer Nebel im Sternbild Segel des Schiffs am S dsternhimmel. Er ist etwa 2000 Lichtjahre von der Sonne entfernt, hat einen Durchmesser von fast einem halben Lichtjahr und expandiert mit einer Geschwindigkeit von rund 15 Kilometern pro Sekunde.');
INSERT INTO ASTROSPHERE.NEBEL(GALAXIE_ID, NAME, DURCHMESSER_LJ, MASSE_KG, ENTFERNUNG_LJ, INFORMATIONEN) VALUES
(1, 'Orionnebel', 24, 1.39237E33, 1350, 'Der Orionnebel ist ein Emissionsnebel im Sternbild Orion. Er befindet sich   wie das Sonnensystem selbst   im Orionarm der Milchstraße.');
INSERT INTO ASTROSPHERE.NEBEL(GALAXIE_ID, NAME, DURCHMESSER_LJ, MASSE_KG, ENTFERNUNG_LJ, INFORMATIONEN) VALUES
(1, 'Lambda-Centauri-Nebel', NULL, NULL, 6500, 'Der Lambda-Centauri-Nebel ist ein Emissionsnebel mit eingebettetem Sternhaufen im Sternbild Zentaur am S dsternhimmel.');
INSERT INTO ASTROSPHERE.NEBEL(GALAXIE_ID, NAME, DURCHMESSER_LJ, MASSE_KG, ENTFERNUNG_LJ, INFORMATIONEN) VALUES
(1, 'Carinanebel', 250, NULL, 8500, 'Der Carinanebel, auch Eta-Carinae-Nebel, ist ein Emissionsnebel im Sternbild Kiel des Schiffs. Eine Aufnahme des Carinanebels war unter den ersten fünf Bildern des James-Webb-Weltraumteleskop, die 2022 der  ffentlichkeit vorgestellt wurden.');


--
-- Inserting data into table ASTROSPHERE.KOMET
--
INSERT INTO ASTROSPHERE.KOMET(NAME, GALAXIE_ID, DURCHMESSER_KM, MASSE_KG, UMLAUFZEIT_J, INFORMATIONEN) VALUES
('Halley', 1, 7.2, 2E14, 75.32, 'Der Komet Halley, auch Halleyscher Komet, zählt seit langem zu den bekanntesten Kometen. Er ist sehr lichtstark und kehrt im Mittel alle 75,3 Jahre wieder. Zuletzt kam er 1986 in Erdn he; seine nächste Wiederkehr wurde für das Jahr 2061 berechnet.');
INSERT INTO ASTROSPHERE.KOMET(NAME, GALAXIE_ID, DURCHMESSER_KM, MASSE_KG, UMLAUFZEIT_J, INFORMATIONEN) VALUES
('Encke', 1, 4.8, NULL, 3.3, 'Der Enckesche Komet ist ein nach Johann Franz Encke benannter kurzperiodischer Komet. Er hat eine der k rzesten Umlaufzeiten aller bekannten Kometen.');
INSERT INTO ASTROSPHERE.KOMET(NAME, GALAXIE_ID, DURCHMESSER_KM, MASSE_KG, UMLAUFZEIT_J, INFORMATIONEN) VALUES
('Biela', 1, NULL, NULL, 6.65, 'Biela (auch Bielascher Komet genannt) war ein Komet, der zwischen 1772 und 1832 viermal beobachtet worden war. Bei seiner erneuten Wiederkehr 1846 wurde festgestellt, dass er in zwei Teile zerbrochen war, die dann 1852 noch einmal beobachtet werden konnten. Seither wurde nichts mehr von diesem Kometen gesehen, er gilt als verloren.');
INSERT INTO ASTROSPHERE.KOMET(NAME, GALAXIE_ID, DURCHMESSER_KM, MASSE_KG, UMLAUFZEIT_J, INFORMATIONEN) VALUES
('Faye', 1, NULL, NULL, 7.55, 'Faye ist ein kurzperiodischer Komet, der von Herv  Faye am 22. November 1843 entdeckt wurde. Er wurde seitdem bei jeder Wiederkehr bis auf 1903 und 1917 beobachtet.');


--
-- Inserting data into table ASTROSPHERE.PLANETENSYSTEM
--
INSERT INTO ASTROSPHERE.PLANETENSYSTEM(GALAXIE_ID, NAME, INFORMATIONEN) VALUES
(1, 'Sonnensystem', 'Das (auch unser) Sonnensystem ist das Planetensystem, in dem sich die Erde befindet. Es besteht aus der Sonne, acht sie umkreisenden Planeten, deren natürlichen Satelliten, den Zwergplaneten, anderen Kleinkörpern und aus unzähligen Gas- und Staubteilchen, die durch die Anziehungskraft der Sonne an diese gebunden sind.');
INSERT INTO ASTROSPHERE.PLANETENSYSTEM(GALAXIE_ID, NAME, INFORMATIONEN) VALUES
(1, 'Alpha Centauri', 'Alpha Centauri ist im Sternbild des Zentauren am Südhimmel ein etwa 4 Lichtjahre entferntes Doppelsternsystem. Es bildet zusammen mit dem ihn umkreisenden, sonnennächsten Roten Zwerg Proxima Centauri ein hierarchisches Dreifachsternsystem.');
INSERT INTO ASTROSPHERE.PLANETENSYSTEM(GALAXIE_ID, NAME, INFORMATIONEN) VALUES
(1, 'Luhman 16', 'Luhman 16 ist ein sonnennahes Doppelsystem von Braunen Zwergen im Sternbild Vela. Das System wurde 2013 von Kevin Luhman mit Hilfe von Daten des Wide-Field Infrared Survey Explorer (WISE) entdeckt.');


--
-- Inserting data into table ASTROSPHERE.RAUM
--
INSERT INTO ASTROSPHERE.RAUM(ABTEILUNG_ID, BEZEICHNUNG, KAPAZITAT, MIET_PREIS) VALUES
(1, 'Merch Shop', 4, NULL);
INSERT INTO ASTROSPHERE.RAUM(ABTEILUNG_ID, BEZEICHNUNG, KAPAZITAT, MIET_PREIS) VALUES
(1, 'Snack Shop', 3, NULL);
INSERT INTO ASTROSPHERE.RAUM(ABTEILUNG_ID, BEZEICHNUNG, KAPAZITAT, MIET_PREIS) VALUES
(2, 'Büro Einkauf', 8, NULL);
INSERT INTO ASTROSPHERE.RAUM(ABTEILUNG_ID, BEZEICHNUNG, KAPAZITAT, MIET_PREIS) VALUES
(3, 'Büro Marketing', 8, NULL);
INSERT INTO ASTROSPHERE.RAUM(ABTEILUNG_ID, BEZEICHNUNG, KAPAZITAT, MIET_PREIS) VALUES
(4, 'Büro IT', 8, NULL);
INSERT INTO ASTROSPHERE.RAUM(ABTEILUNG_ID, BEZEICHNUNG, KAPAZITAT, MIET_PREIS) VALUES
(5, 'Veranstaltungsraum 1', 20, 299.99);
INSERT INTO ASTROSPHERE.RAUM(ABTEILUNG_ID, BEZEICHNUNG, KAPAZITAT, MIET_PREIS) VALUES
(5, 'Veranstaltungsraum 2', 50, 499.99);
INSERT INTO ASTROSPHERE.RAUM(ABTEILUNG_ID, BEZEICHNUNG, KAPAZITAT, MIET_PREIS) VALUES
(5, 'Veranstaltungsraum 3', 60, 599.99);
INSERT INTO ASTROSPHERE.RAUM(ABTEILUNG_ID, BEZEICHNUNG, KAPAZITAT, MIET_PREIS) VALUES
(5, 'Veranstaltungsraum 4', 70, 699.99);
INSERT INTO ASTROSPHERE.RAUM(ABTEILUNG_ID, BEZEICHNUNG, KAPAZITAT, MIET_PREIS) VALUES
(5, 'Veranstaltungsraum 5', 80, 799.99);
INSERT INTO ASTROSPHERE.RAUM(ABTEILUNG_ID, BEZEICHNUNG, KAPAZITAT, MIET_PREIS) VALUES
(5,'Veranstaltungsraum 6', 100, 899.99);
INSERT INTO ASTROSPHERE.RAUM(ABTEILUNG_ID, BEZEICHNUNG, KAPAZITAT, MIET_PREIS) VALUES
(6,'Sicherheit 1', 6, NULL);
INSERT INTO ASTROSPHERE.RAUM(ABTEILUNG_ID, BEZEICHNUNG, KAPAZITAT, MIET_PREIS) VALUES
(7,'Labor 1', 10, NULL);
INSERT INTO ASTROSPHERE.RAUM(ABTEILUNG_ID, BEZEICHNUNG, KAPAZITAT, MIET_PREIS) VALUES
(7,'Labor 2', 10, NULL);
INSERT INTO ASTROSPHERE.RAUM(ABTEILUNG_ID, BEZEICHNUNG, KAPAZITAT, MIET_PREIS) VALUES
(7,'Labor 3', 10, NULL);
INSERT INTO ASTROSPHERE.RAUM(ABTEILUNG_ID, BEZEICHNUNG, KAPAZITAT, MIET_PREIS) VALUES
(8,'Büro Vermietung', 5, NULL);
INSERT INTO ASTROSPHERE.RAUM(ABTEILUNG_ID, BEZEICHNUNG, KAPAZITAT, MIET_PREIS) VALUES
(8,'Büro Vermietung', 5, NULL);
INSERT INTO ASTROSPHERE.RAUM(ABTEILUNG_ID, BEZEICHNUNG, KAPAZITAT, MIET_PREIS) VALUES
(8,'Büro Personalabteilung', 5, NULL);
INSERT INTO ASTROSPHERE.RAUM(ABTEILUNG_ID, BEZEICHNUNG, KAPAZITAT, MIET_PREIS) VALUES
(8,'Büro Finanzen', 5, NULL);
INSERT INTO ASTROSPHERE.RAUM(ABTEILUNG_ID, BEZEICHNUNG, KAPAZITAT, MIET_PREIS) VALUES
(8,'Büro Design', 5, NULL);


--
-- Inserting data into table ASTROSPHERE.PLANET
--
INSERT INTO ASTROSPHERE.PLANET(PLANETENSYSTEM_ID, ZENTRUMSPLANET_ID, NAME, DURCHMESSER_KM, MASSE_KG, UMLAUFZEIT_TAGE, TEMPERATUR_CELSIUS, FALLBESCHLEUNIGUNG, INFORMATIONEN) VALUES
(1, NULL, 'Merkur', 4879, 3.3011E23, 87.89, 167, 3.7, 'Der Merkur ist mit einem Durchmesser von knapp 4880 Kilometern der kleinste, mit einer durchschnittlichen Sonnenentfernung von etwa 58 Millionen Kilometern der sonnennächste und somit auch schnellste Planet im Sonnensystem.');
INSERT INTO ASTROSPHERE.PLANET(PLANETENSYSTEM_ID, ZENTRUMSPLANET_ID, NAME, DURCHMESSER_KM, MASSE_KG, UMLAUFZEIT_TAGE, TEMPERATUR_CELSIUS, FALLBESCHLEUNIGUNG, INFORMATIONEN) VALUES
(1, NULL, 'Venus', 12104, 4.8675E24, 224.7, 464, 8.87, 'Die Venus ist mit einer durchschnittlichen Sonnenentfernung von 108 Millionen Kilometern der zweitinnerste und mit einem Durchmesser von ca. 12.100 Kilometern der drittkleinste Planet des Sonnensystems. Sie zählt zu den vier erdähnlichen Planeten, die auch terrestrische oder Gesteinsplaneten genannt werden.');
INSERT INTO ASTROSPHERE.PLANET(PLANETENSYSTEM_ID, ZENTRUMSPLANET_ID, NAME, DURCHMESSER_KM, MASSE_KG, UMLAUFZEIT_TAGE, TEMPERATUR_CELSIUS, FALLBESCHLEUNIGUNG, INFORMATIONEN) VALUES
(1, NULL, 'Erde', 12742, 5.97219E24, 365.25, 15, 9.81, 'Die Erde ist der fünftgrößte und der Sonne drittnächste Planet des Sonnensystems. Sie bewegt sich auf einer elliptischen Bahn um die Sonne.');
INSERT INTO ASTROSPHERE.PLANET(PLANETENSYSTEM_ID, ZENTRUMSPLANET_ID, NAME, DURCHMESSER_KM, MASSE_KG, UMLAUFZEIT_TAGE, TEMPERATUR_CELSIUS, FALLBESCHLEUNIGUNG, INFORMATIONEN) VALUES
(1, NULL, 'Mars', 6779, 6.4171E23, 687, -65, 3.73, 'Der Mars ist, von der Sonne aus gezählt, der vierte Planet im Sonnensystem und der äußere Nachbar der Erde. Er zählt zu den erdähnlichen (terrestrischen) Planeten. Sein Durchmesser ist mit knapp 6800 Kilometern etwa halb so groß wie der der Erde, sein Volumen beträgt gut ein Siebtel des Erdvolumens. Damit ist der Mars nach dem Merkur der zweitkleinste Planet des Sonnensystems, hat jedoch eine vielfältige Geologie und die höchsten Vulkane des Sonnensystems.');
INSERT INTO ASTROSPHERE.PLANET(PLANETENSYSTEM_ID, ZENTRUMSPLANET_ID, NAME, DURCHMESSER_KM, MASSE_KG, UMLAUFZEIT_TAGE, TEMPERATUR_CELSIUS, FALLBESCHLEUNIGUNG, INFORMATIONEN) VALUES
(1, NULL, 'Jupiter', 139820, 1.89813E27, 4331, -110, 24.79, 'Jupiter ist mit einem Äquatordurchmesser von rund 143.000 Kilometern der größte Planet des Sonnensystems. Mit einer durchschnittlichen Entfernung von 778 Millionen Kilometern ist er von der Sonne aus gesehen der fünfte Planet. Er ist nach dem römischen Hauptgott Jupiter benannt. Der Planet hat, wie auch Saturn, Uranus und Neptun keine feste Oberfläche. Die schon im kleinen Fernrohr sichtbaren, fast parallelen Streifen sind farbige Wolkenbänder. Aufgrund seiner chemischen Zusammensetzung zählt Jupiter zu den Gasplaneten.');
INSERT INTO ASTROSPHERE.PLANET(PLANETENSYSTEM_ID, ZENTRUMSPLANET_ID, NAME, DURCHMESSER_KM, MASSE_KG, UMLAUFZEIT_TAGE, TEMPERATUR_CELSIUS, FALLBESCHLEUNIGUNG, INFORMATIONEN) VALUES
(1, NULL, 'Saturn', 116460, 5.68319E26, 10747, -140, 10.44, 'Der Saturn ist von der Sonne aus gesehen der sechste Planet des Sonnensystems und mit einem Äquatordurchmesser von etwa 120.500 Kilometern (9,5-facher Erddurchmesser) nach Jupiter der zweitgrößte. Mit 95 Erdmassen hat er jedoch nur 30 % der Masse Jupiters. Wegen seines auffallenden und schon im kleinen Fernrohr sichtbaren Ringsystems wird er oft auch der Ringplanet genannt, obwohl auch bei den anderen drei Gasplaneten Ringsysteme gefunden wurden.');
INSERT INTO ASTROSPHERE.PLANET(PLANETENSYSTEM_ID, ZENTRUMSPLANET_ID, NAME, DURCHMESSER_KM, MASSE_KG, UMLAUFZEIT_TAGE, TEMPERATUR_CELSIUS, FALLBESCHLEUNIGUNG, INFORMATIONEN) VALUES
(1, NULL, 'Uranus', 50724, 8.68103E25, 30589, -195, 8.87, 'Der Uranus ist von der Sonne aus mit einer durchschnittlichen Sonnenentfernung von 2,9 Milliarden Kilometern der siebte Planet im Sonnensystem und wird zu den Eisriesen gerechnet.');
INSERT INTO ASTROSPHERE.PLANET(PLANETENSYSTEM_ID, ZENTRUMSPLANET_ID, NAME, DURCHMESSER_KM, MASSE_KG, UMLAUFZEIT_TAGE, TEMPERATUR_CELSIUS, FALLBESCHLEUNIGUNG, INFORMATIONEN) VALUES
(1, NULL, 'Neptun', 49244, 1.0241E26, 59800, -200, 11.15, 'Der Neptun ist der achte und äußerste bekannte Planet unseres Sonnensystems. Nach Jupiter, Saturn und Uranus ist Neptun der viertgrößte Planet des Sonnensystems. Zusammen mit Uranus bildet Neptun die Untergruppe der Eisriesen.');
INSERT INTO ASTROSPHERE.PLANET(PLANETENSYSTEM_ID, ZENTRUMSPLANET_ID, NAME, DURCHMESSER_KM, MASSE_KG, UMLAUFZEIT_TAGE, TEMPERATUR_CELSIUS, FALLBESCHLEUNIGUNG, INFORMATIONEN) VALUES
(2, NULL, 'Proxima Centauri b', 14016.2, 6.987474E24, 11.184, -39, NULL, 'Proxima Centauri b ist der nach aktuellem Forschungsstand erdnächste erwiesene Exoplanet. Er umkreist den etwa 4,2 Lichtjahre von der Erde entfernten Stern Proxima Centauri innerhalb dessen habitabler Zone und wurde im August 2016 mit der Radialgeschwindigkeitsmethode nachgewiesen. Auf ihm k nnte flüssiges Wasser existieren, eine wichtige Voraussetzung für erdähnliches Leben.');
INSERT INTO ASTROSPHERE.PLANET(PLANETENSYSTEM_ID, ZENTRUMSPLANET_ID, NAME, DURCHMESSER_KM, MASSE_KG, UMLAUFZEIT_TAGE, TEMPERATUR_CELSIUS, FALLBESCHLEUNIGUNG, INFORMATIONEN) VALUES
(2, NULL, 'Proxima Centauri c', 22948.932, 4.18054E25, 1928, -234, NULL, 'Proxima Centauri c ist ein Exoplanet, der gemeinsam mit Proxima Centauri b den roten Zwergstern Proxima Centauri, welcher der Sonne am nächsten gelegen und Teil eines Dreifachsternsystems ist, umkreist.');
INSERT INTO ASTROSPHERE.PLANET(PLANETENSYSTEM_ID, ZENTRUMSPLANET_ID, NAME, DURCHMESSER_KM, MASSE_KG, UMLAUFZEIT_TAGE, TEMPERATUR_CELSIUS, FALLBESCHLEUNIGUNG, INFORMATIONEN) VALUES
(1, 3, 'Mond', 3476 , 7.346E21, 27.3217, -30.65, 1.62, 'Der Mond ist der einzige natürliche Satellit der Erde. Sein Name ist etymologisch verwandt mit Monat. Weil die Trabanten anderer Planeten des Sonnensystems im übertragenen Sinn meist ebenfalls als Monde bezeichnet werden, spricht man zur Vermeidung von Verwechslungen mitunter vom Erdmond.');
INSERT INTO ASTROSPHERE.PLANET(PLANETENSYSTEM_ID, ZENTRUMSPLANET_ID, NAME, DURCHMESSER_KM, MASSE_KG, UMLAUFZEIT_TAGE, TEMPERATUR_CELSIUS, FALLBESCHLEUNIGUNG, INFORMATIONEN) VALUES
(1, 5, 'Io', 3643, 8.9E22, 1.77, -143, 1.796, 'Io ist der innerste der vier Galileischen Monde und zeichnet sich durch seine vulkanische Aktivität aus. Seine Oberfläche ist von aktiven Vulkanen, Schwefeldioxid-Eis und farbenfrohen Ablagerungen geprägt');
INSERT INTO ASTROSPHERE.PLANET(PLANETENSYSTEM_ID, ZENTRUMSPLANET_ID, NAME, DURCHMESSER_KM, MASSE_KG, UMLAUFZEIT_TAGE, TEMPERATUR_CELSIUS, FALLBESCHLEUNIGUNG, INFORMATIONEN) VALUES
(1, 5, 'Europa', 3122, 4.8E22, 3.55, -160, 1.314, 'Europa ist für seine eisbedeckte Oberfläche und den vermuteten Ozean unter der Eisschicht bekannt. Wissenschaftler vermuten, dass dieser Ozean flüssiges Wasser und möglicherweise Lebensbedingungen beherbergt');
INSERT INTO ASTROSPHERE.PLANET(PLANETENSYSTEM_ID, ZENTRUMSPLANET_ID, NAME, DURCHMESSER_KM, MASSE_KG, UMLAUFZEIT_TAGE, TEMPERATUR_CELSIUS, FALLBESCHLEUNIGUNG, INFORMATIONEN) VALUES
(1, 5, 'Ganymed', 5262, 1.5E23, 7.16, -160, 1.428, 'Ganymed ist der größte Mond im Sonnensystem und sogar größer als der Planet Merkur. Seine Oberfläche besteht aus einer Mischung aus Eis und Gestein, und er besitzt einen eigenen Magnetfeld');
INSERT INTO ASTROSPHERE.PLANET(PLANETENSYSTEM_ID, ZENTRUMSPLANET_ID, NAME, DURCHMESSER_KM, MASSE_KG, UMLAUFZEIT_TAGE, TEMPERATUR_CELSIUS, FALLBESCHLEUNIGUNG, INFORMATIONEN) VALUES
(1, 5, 'Callisto', 4820, 1.0759E23, 16.69, -145, 1.235, 'Callisto ist der vierte (äußerste) der vier großen Galileischen Monde des Jupiters. Mit seinem Durchmesser von 4820 km ist er der drittgrößte Mond im Sonnensystem und nur geringfügig kleiner als der Planet Merkur. Callisto ist ein Eismond und weist eine stark zerklüftete Oberfläche mit zahlreichen Kratern auf. Es ist der kraterreichste körper im Sonnensystem. Außerdem ist Callisto der äußerste der vier Galileischen Monde und hat eine sehr dünne Atmosphäre, die hauptsächlich aus Kohlendioxid besteht');
INSERT INTO ASTROSPHERE.PLANET(PLANETENSYSTEM_ID, ZENTRUMSPLANET_ID, NAME, DURCHMESSER_KM, MASSE_KG, UMLAUFZEIT_TAGE, TEMPERATUR_CELSIUS, FALLBESCHLEUNIGUNG, INFORMATIONEN) VALUES
(1, 6, 'Titan', 5150, 1.3E23, 15.95, -180, 1.35, 'Titan ist der größte Mond des Saturns und besitzt eine dichte Atmosphäre, die hauptsächlich aus Stickstoff besteht. Seine Oberfläche ist mit Seen und Flüssen aus flüssigem Methan und Ethan bedeckt');
INSERT INTO ASTROSPHERE.PLANET(PLANETENSYSTEM_ID, ZENTRUMSPLANET_ID, NAME, DURCHMESSER_KM, MASSE_KG, UMLAUFZEIT_TAGE, TEMPERATUR_CELSIUS, FALLBESCHLEUNIGUNG, INFORMATIONEN) VALUES
(1, 6, 'Enceladus', 499, 1.08E20, 1.37, -128, 1.35, 'Enceladus ist für seine eisigen Geysire bekannt, die Wasser und andere Materialien aus seinem Inneren ins All sprühen. Diese Geysire deuten auf einen möglichen unterirdischen Ozean hin');
INSERT INTO ASTROSPHERE.PLANET(PLANETENSYSTEM_ID, ZENTRUMSPLANET_ID, NAME, DURCHMESSER_KM, MASSE_KG, UMLAUFZEIT_TAGE, TEMPERATUR_CELSIUS, FALLBESCHLEUNIGUNG, INFORMATIONEN) VALUES
(1, 6, 'Iapetus', 1436, 2E21, 79.33, -140, 1.35, 'Iapetus hat eine ungewöhnliche zweifarbige Oberfläche: Eine Hemisphäre ist hell und die andere dunkel. Dieses Phänomen ist noch nicht vollständig verstanden');


--
-- Inserting data into table ASTROSPHERE.STERN
--
INSERT INTO ASTROSPHERE.STERN(STERNENBILD_ID, PLANETENSYSTEM_ID, NAME, TYP, DURCHMESSER_KM, MASSE_KG, ENTFERNUNG_LJ, INFORMATIONEN) VALUES
(NULL, 1, 'Sonne', 'Gelber Zwerck', 13926844, 1.9884E30, 1.58E-5, 'Die Sonne ist der Stern, der der Erde am nächsten ist und das Zentrum des Sonnensystems bildet. Sie ist ein durchschnittlich großer Stern im äußeren Drittel der Milchstraße. Die Sonne ist ein Zwergstern, der sich im Entwicklungsstadium der Hauptreihe befindet.');
INSERT INTO ASTROSPHERE.STERN(STERNENBILD_ID, PLANETENSYSTEM_ID, NAME, TYP, DURCHMESSER_KM, MASSE_KG, ENTFERNUNG_LJ, INFORMATIONEN) VALUES
(14, 2, 'Alpha Centauri A', 'Gelber Zwerck', 16990749.68, 2.18801E30, 4.344, 'Alpha Centauri A ist wie die Sonne ein Gelber Zwerg, damit gehört er wie die Sonne zu den hei eren G-Sternen. Da Alpha Centauri A vom gleichen Spektraltyp ist und ähnliche Dimensionen wie die Sonne hat, gilt er als der erdnächste  Sonnenzwilling  (was aber nicht bedeutet, dass sie zusammen entstanden sind). Seine Oberflächentemperatur beträgt etwa 5800 K.');
INSERT INTO ASTROSPHERE.STERN(STERNENBILD_ID, PLANETENSYSTEM_ID, NAME, TYP, DURCHMESSER_KM, MASSE_KG, ENTFERNUNG_LJ, INFORMATIONEN) VALUES
(14, 3, 'Alpha Centauri B', NULL, 11977085.84, 1.849863E30, 4.344, 'Alpha Centauri B ist die Nummer 21 in der Liste der hellsten Sterne am Himmel. Mit einer Oberflächentemperatur von etwa 5300 K ist er nur wenig kühler als die Sonne. Er erreicht wegen der geringeren Temperatur und der kleineren Oberfläche jedoch nur 50 % der Sonnenstrahlungsleistung.');
INSERT INTO ASTROSPHERE.STERN(STERNENBILD_ID, PLANETENSYSTEM_ID, NAME, TYP, DURCHMESSER_KM, MASSE_KG, ENTFERNUNG_LJ, INFORMATIONEN) VALUES
(14, 3, 'Proxima Centauri', 'Roter Zwerck', 2E5, 2.446593E29, 4.2465, 'Proxima Centauri, auch V645 Centauri oder Alpha Centauri C genannt, ist mit einer Entfernung von etwa 4,247 Lichtjahren der Sonne nächstgelegene Stern. Er wurde im Sternenbild des Zentauren entdeckt. Proxima Centauri umkreist Alpha Centauri A und Alpha Centauri B innerhalb von 591.000 Jahren. Die drei Sterne bilden zusammen ein hierarchisches Dreifachsternensystem.');
INSERT INTO ASTROSPHERE.STERN(STERNENBILD_ID, PLANETENSYSTEM_ID, NAME, TYP, DURCHMESSER_KM, MASSE_KG, ENTFERNUNG_LJ, INFORMATIONEN) VALUES
(12, NULL, 'Barnards Pfeilstern', 'Roter Zwerck', 2.699316E5, 3.18256E29, 5.9629, 'Barnards Pfeilstern ist ein kleiner Stern im Sternbild Schlangenträger. Mit einer Entfernung von etwa 6 Lichtjahren ist Barnards Pfeilstern unter den bekannten Sternen der dem Sonnensystem viertnächste. Nur die drei Komponenten des Alpha-Centauri-Systems liegen näher.');


--
-- Inserting data into table ASTROSPHERE.VERKAUF
--
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(13, 27, NULL, '06/08/2005 09:15:57');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(1, 38, 0.25, '02/12/1980 04:29:22');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(1, 11, NULL, '01/01/1970 00:00:07');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(6, 1, NULL, '10/27/2005 23:54:04');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(17, 1, NULL, '12/24/2000 16:59:22');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(21, 45, NULL, '11/22/2008 07:17:39');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(1, 12, 0.32, '01/21/1990 22:55:58');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(2, 47, NULL, '08/25/1983 03:24:00');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(25, 16, NULL, '07/04/2008 03:48:37');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(16, 6, NULL, '12/16/1995 02:14:07');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(13, 16, NULL, '09/02/1987 12:22:42');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(17, 29, 0.08, '01/01/1970 00:01:09');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(3, 14, NULL, '03/07/1992 13:40:11');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(11, 25, 0.05, '01/01/1970 00:02:42');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(14, 28, 0.03, '01/01/1970 02:01:11');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(22, 24, NULL, '03/05/2017 00:41:31');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(5, 31, 0.02, '10/26/2005 11:32:06');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(12, 10, NULL, '08/12/2015 10:55:35');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(1, 9, NULL, '02/24/2015 10:50:34');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(1, 23, NULL, '10/15/1973 09:28:34');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(12, 42, 0.06, '01/13/2020 01:34:22');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(18, 6, NULL, '09/28/1982 17:21:25');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(21, 40, NULL, '12/07/2019 12:36:54');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(25, 23, 0.12, '06/13/2002 23:08:37');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(2, 45, NULL, '07/20/2009 17:56:55');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(19, 19, NULL, '09/20/1994 06:14:42');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(5, 39, NULL, '07/20/1998 08:59:31');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(23, 12, NULL, '11/11/2002 13:57:32');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(9, 50, NULL, '08/22/1988 08:09:37');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(20, 10, NULL, '09/21/1981 21:51:41');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(1, 32, 0.16, '12/28/2020 23:26:54');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(18, 35, 0.10, '10/26/2022 18:37:34');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(12, 19, NULL, '05/24/2010 00:26:30');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(11, 46, NULL, '04/07/2006 18:14:38');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(4, 22, NULL, '05/09/1987 22:30:24');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(18, 15, NULL, '01/01/1970 00:00:02');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(24, 15, 0.08, '11/07/1989 13:32:03');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(1, 12, NULL, '03/16/2000 21:29:59');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(22, 1, NULL, '01/01/1970 01:25:23');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(18, 8, NULL, '02/08/2011 03:01:16');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(13, 20, NULL, '01/01/1970 00:00:03');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(4, 29, 0.11, '02/15/2005 13:02:20');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(14, 33, 0.14, '01/01/1970 00:00:25');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(19, 6, 0.10, '01/01/1970 00:00:03');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(25, 43, 0.20, '11/30/1973 10:15:38');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(14, 44, 0.05, '12/19/2017 01:42:26');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(17, 44, 0.11, '01/04/1978 21:42:12');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(9, 41, 0.23, '05/04/1976 07:39:50');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(1, 24, 0.18, '10/26/2003 22:41:41');
INSERT INTO ASTROSPHERE.VERKAUF(KUNDE_ID, ANGESTELLTER_ID, RABATT, DATUM) VALUES
(1, 28, 0.06, '04/02/1973 00:56:04');


--
-- Inserting data into table ASTROSPHERE.VERKAUF_TICKETSTUFE
--
INSERT INTO ASTROSPHERE.VERKAUF_TICKETSTUFE(VERKAUF_ID, STUFE, ANZAHL) VALUES
(2, 'Tag', 2);
INSERT INTO ASTROSPHERE.VERKAUF_TICKETSTUFE(VERKAUF_ID, STUFE, ANZAHL) VALUES
(3, 'Tag', 5);
INSERT INTO ASTROSPHERE.VERKAUF_TICKETSTUFE(VERKAUF_ID, STUFE, ANZAHL) VALUES
(7, 'Tag', 3);
INSERT INTO ASTROSPHERE.VERKAUF_TICKETSTUFE(VERKAUF_ID, STUFE, ANZAHL) VALUES
(8, 'Monat', 1);
INSERT INTO ASTROSPHERE.VERKAUF_TICKETSTUFE(VERKAUF_ID, STUFE, ANZAHL) VALUES
(10, 'Monat', 1);
INSERT INTO ASTROSPHERE.VERKAUF_TICKETSTUFE(VERKAUF_ID, STUFE, ANZAHL) VALUES
(11, 'Jahr', 2);
INSERT INTO ASTROSPHERE.VERKAUF_TICKETSTUFE(VERKAUF_ID, STUFE, ANZAHL) VALUES
(15, 'Monat', 9);
INSERT INTO ASTROSPHERE.VERKAUF_TICKETSTUFE(VERKAUF_ID, STUFE, ANZAHL) VALUES
(16, 'Jahr', 4);
INSERT INTO ASTROSPHERE.VERKAUF_TICKETSTUFE(VERKAUF_ID, STUFE, ANZAHL) VALUES
(17, 'Jahr', 8);
INSERT INTO ASTROSPHERE.VERKAUF_TICKETSTUFE(VERKAUF_ID, STUFE, ANZAHL) VALUES
(19, 'Tag', 1);
INSERT INTO ASTROSPHERE.VERKAUF_TICKETSTUFE(VERKAUF_ID, STUFE, ANZAHL) VALUES
(20, 'Tag', 2);
INSERT INTO ASTROSPHERE.VERKAUF_TICKETSTUFE(VERKAUF_ID, STUFE, ANZAHL) VALUES
(22, 'Jahr', 3);
INSERT INTO ASTROSPHERE.VERKAUF_TICKETSTUFE(VERKAUF_ID, STUFE, ANZAHL) VALUES
(24, 'Monat', 4);
INSERT INTO ASTROSPHERE.VERKAUF_TICKETSTUFE(VERKAUF_ID, STUFE, ANZAHL) VALUES
(26, 'Monat', 5);
INSERT INTO ASTROSPHERE.VERKAUF_TICKETSTUFE(VERKAUF_ID, STUFE, ANZAHL) VALUES
(31, 'Tag', 6);
INSERT INTO ASTROSPHERE.VERKAUF_TICKETSTUFE(VERKAUF_ID, STUFE, ANZAHL) VALUES
(38, 'Tag', 7);
INSERT INTO ASTROSPHERE.VERKAUF_TICKETSTUFE(VERKAUF_ID, STUFE, ANZAHL) VALUES
(39, 'Monat', 8);
INSERT INTO ASTROSPHERE.VERKAUF_TICKETSTUFE(VERKAUF_ID, STUFE, ANZAHL) VALUES
(40, 'Jahr', 9);
INSERT INTO ASTROSPHERE.VERKAUF_TICKETSTUFE(VERKAUF_ID, STUFE, ANZAHL) VALUES
(41, 'Jahr', 3);
INSERT INTO ASTROSPHERE.VERKAUF_TICKETSTUFE(VERKAUF_ID, STUFE, ANZAHL) VALUES
(42, 'Monat', 2);
INSERT INTO ASTROSPHERE.VERKAUF_TICKETSTUFE(VERKAUF_ID, STUFE, ANZAHL) VALUES
(44, 'Monat', 1);
INSERT INTO ASTROSPHERE.VERKAUF_TICKETSTUFE(VERKAUF_ID, STUFE, ANZAHL) VALUES
(45, 'Jahr', 1);
INSERT INTO ASTROSPHERE.VERKAUF_TICKETSTUFE(VERKAUF_ID, STUFE, ANZAHL) VALUES
(48, 'Monat', 1);
INSERT INTO ASTROSPHERE.VERKAUF_TICKETSTUFE(VERKAUF_ID, STUFE, ANZAHL) VALUES
(49, 'Tag', 1);
INSERT INTO ASTROSPHERE.VERKAUF_TICKETSTUFE(VERKAUF_ID, STUFE, ANZAHL) VALUES
(50, 'Tag', 1);


--
-- Inserting data into table ASTROSPHERE.MEDIUM
--
INSERT INTO ASTROSPHERE.MEDIUM(GALAXIE_ID, PLANET_ID, PLANETENSYSTEM_ID, NEBEL_ID, STERN_ID, STERNENBILD_ID, KOMET_ID, FORMAT, TYP, IMAGE_PATH) VALUES
(NULL, NULL, NULL, 5, 3, NULL, 1, 'gif', 'Video', '..static/images/planets/carinanebel.png');
INSERT INTO ASTROSPHERE.MEDIUM(GALAXIE_ID, PLANET_ID, PLANETENSYSTEM_ID, NEBEL_ID, STERN_ID, STERNENBILD_ID, KOMET_ID, FORMAT, TYP, IMAGE_PATH) VALUES
(1, NULL, 3, NULL, NULL, 2, NULL, 'mp3', 'Audio', '..static/images/planets/milchstrasse.png');
INSERT INTO ASTROSPHERE.MEDIUM(GALAXIE_ID, PLANET_ID, PLANETENSYSTEM_ID, NEBEL_ID, STERN_ID, STERNENBILD_ID, KOMET_ID, FORMAT, TYP, IMAGE_PATH) VALUES
(2, NULL, NULL, 5, NULL, 2, 1, 'pdf', 'Dokument', '..static/images/planets/andromeda_galaxy.png');
INSERT INTO ASTROSPHERE.MEDIUM(GALAXIE_ID, PLANET_ID, PLANETENSYSTEM_ID, NEBEL_ID, STERN_ID, STERNENBILD_ID, KOMET_ID, FORMAT, TYP, IMAGE_PATH) VALUES
(1, NULL, NULL, NULL, NULL, 2, 2, 'jpeg', 'Bild', '..static/images/planets/alpha_centauri_a.png.png');
INSERT INTO ASTROSPHERE.MEDIUM(GALAXIE_ID, PLANET_ID, PLANETENSYSTEM_ID, NEBEL_ID, STERN_ID, STERNENBILD_ID, KOMET_ID, FORMAT, TYP, IMAGE_PATH) VALUES
(2, 3, NULL, 5, NULL, 3, 3, 'png', 'Bild', '..static/images/planets/erde.png');
INSERT INTO ASTROSPHERE.MEDIUM(GALAXIE_ID, PLANET_ID, PLANETENSYSTEM_ID, NEBEL_ID, STERN_ID, STERNENBILD_ID, KOMET_ID, FORMAT, TYP, IMAGE_PATH) VALUES
(2, 10, NULL, 4, 1, 1, 3, 'gif', 'Video', '..static/images/planets/proxima_b.png');
INSERT INTO ASTROSPHERE.MEDIUM(GALAXIE_ID, PLANET_ID, PLANETENSYSTEM_ID, NEBEL_ID, STERN_ID, STERNENBILD_ID, KOMET_ID, FORMAT, TYP, IMAGE_PATH) VALUES
(1, 4, NULL, 4, 1, 2, 3, 'obj', '3D-Modell', '..static/images/planets/mars.png');
INSERT INTO ASTROSPHERE.MEDIUM(GALAXIE_ID, PLANET_ID, PLANETENSYSTEM_ID, NEBEL_ID, STERN_ID, STERNENBILD_ID, KOMET_ID, FORMAT, TYP, IMAGE_PATH) VALUES
(1, 6, NULL, 4, NULL, 3, 3, 'jpeg', 'Bild', '..static/images/planets/saturn.png');
INSERT INTO ASTROSPHERE.MEDIUM(GALAXIE_ID, PLANET_ID, PLANETENSYSTEM_ID, NEBEL_ID, STERN_ID, STERNENBILD_ID, KOMET_ID, FORMAT, TYP, IMAGE_PATH) VALUES
(1, 2, NULL, 2, NULL, 2, 2, 'png', 'Bild', '..static/images/planets/venus.png');
INSERT INTO ASTROSPHERE.MEDIUM(GALAXIE_ID, PLANET_ID, PLANETENSYSTEM_ID, NEBEL_ID, STERN_ID, STERNENBILD_ID, KOMET_ID, FORMAT, TYP, IMAGE_PATH) VALUES
(1, NULL, NULL, 2, 1, 3, 1, 'mp3', 'Audio', '..static/images/planets/sonne.png');
INSERT INTO ASTROSPHERE.MEDIUM(GALAXIE_ID, PLANET_ID, PLANETENSYSTEM_ID, NEBEL_ID, STERN_ID, STERNENBILD_ID, KOMET_ID, FORMAT, TYP, IMAGE_PATH) VALUES
(2, 7, NULL, 5, 3, 3, 1, 'mp4', 'Video', '..static/images/planets/uranus.png');
INSERT INTO ASTROSPHERE.MEDIUM(GALAXIE_ID, PLANET_ID, PLANETENSYSTEM_ID, NEBEL_ID, STERN_ID, STERNENBILD_ID, KOMET_ID, FORMAT, TYP, IMAGE_PATH) VALUES
(1, 6, NULL, 1, 2, 2, 3, 'mp4', 'Video', '..static/images/planets/saturn.png');
INSERT INTO ASTROSPHERE.MEDIUM(GALAXIE_ID, PLANET_ID, PLANETENSYSTEM_ID, NEBEL_ID, STERN_ID, STERNENBILD_ID, KOMET_ID, FORMAT, TYP, IMAGE_PATH) VALUES
(1, 8, NULL, 5, 5, 1, 3, 'png', 'Bild', '..static/images/planets/neptun.png');
INSERT INTO ASTROSPHERE.MEDIUM(GALAXIE_ID, PLANET_ID, PLANETENSYSTEM_ID, NEBEL_ID, STERN_ID, STERNENBILD_ID, KOMET_ID, FORMAT, TYP, IMAGE_PATH) VALUES
(2, 9, NULL, 1, 6, 1, 1, 'gif', 'Video', '..static/images/planets/proxima_b.png');


--
-- Inserting data into table ASTROSPHERE.VERANSTALTUNG
--
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(6, 'Sternenreise durch die Galaxie', '07/05/2024 09:00:00', 'Erleben Sie eine faszinierende Reise durch unser Universum, angefangen von den nahen Planeten bis zu den entferntesten Galaxien.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(6, 'Mondnacht im Planetarium', '07/05/2024 15:00:00', 'Eine romantische Nacht unter den Sternen, mit besonderem Fokus auf dem Mond und seinen mystischen Geheimnissen.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(8, 'Kosmische Kollisionen', '07/06/2024 09:00:00', 'Tauchen Sie ein in die Welt der Asteroiden, Kometen und planetaren Kollisionen und erfahren Sie mehr über die beeindruckende Geschichte unseres Sonnensystems.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(7, 'Die Geheimnisse der Schwarzen Löcher', '07/06/2024 15:00:00', 'Eine tiefgehende Erkundung der faszinierenden Phänomene der Schwarzen Löcher und ihrer Auswirkungen auf Raum und Zeit.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(11, 'Kinderplanetarium', '07/07/2024 09:00:00', 'Ein interaktives Erlebnis für die jüngsten Entdecker, um spielerisch die Wunder des Weltraums zu erforschen.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(9, 'Exoplaneten-Expedition', '07/07/2024 15:00:00', 'Begleiten Sie uns auf eine Reise zu den fernen Welten außerhalb unseres Sonnensystems und entdecken Sie potenziell bewohnbare Exoplaneten.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(10, 'Astronomie für Einsteiger', '07/08/2024 09:00:00', 'Eine Einführung in die Grundlagen der Astronomie für Neulinge, die mehr über Sterne, Planeten und den Himmel erfahren möchten.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(10, 'Kunst im Kosmos', '07/08/2024 15:00:00', 'Eine kreative Fusion von Astronomie und Kunst, die die Schönheit des Universums durch visuelle Darstellungen und Projektionen erkundet.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(6, 'Die Geschichte der Raumfahrt', '07/09/2024 09:00:00', 'Eine chronologische Reise durch die Meilensteine der Raumfahrt, von den ersten Satelliten bis zu den aktuellen Marsmissionen.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(8, 'Himmelskonzert', '07/09/2024 15:00:00', 'Genießen Sie eine audiovisuelle Vorführung, bei der Sternbilder und Himmelskörper mit passender Musik harmonisch kombiniert werden.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(6, 'Astronomische R tselrallye', '07/10/2024 09:00:00', 'Ein interaktiver Abend, bei dem die Teilnehmer knifflige astronomische Rätsel lösen und dabei mehr über den Weltraum erfahren.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(7, 'Die Farben des Kosmos', '07/10/2024 15:00:00', 'Eine visuelle Reise, die die verschiedenen Farben im Universum erkundet und erklärt, von leuchtenden Gaswolken bis zu bunten Nebeln.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(7, 'Mars-Expedition live', '07/10/2024 19:00:00', 'Begleiten Sie uns auf eine virtuelle Reise zum Mars und erleben Sie, wie Raumfahrttechnologie diesen fernen Planeten erkundet.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(11, 'Astrofotografie-Workshop', '07/11/2024 09:00:00', 'Lernen Sie die Grundlagen der Astrofotografie und nehmen Sie an einem praktischen Workshop teil, um beeindruckende Himmelsaufnahmen zu erstellen.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(11, 'Die Zukunft der Raumfahrt', '07/11/2024 15:00:00', 'Eine Diskussionsveranstaltung über zukünftige Entwicklungen in der Raumfahrt, von bemannten Marsmissionen bis zu bahnbrechenden Technologien.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(6, 'Sternenreise durch die Galaxie', '07/12/2024 09:00:00', 'Erleben Sie eine faszinierende Reise durch unser Universum, angefangen von den nahen Planeten bis zu den entferntesten Galaxien.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(6, 'Mondnacht im Planetarium', '07/12/2024 15:00:00', 'Eine romantische Nacht unter den Sternen, mit besonderem Fokus auf dem Mond und seinen mystischen Geheimnissen.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(8, 'Kosmische Kollisionen', '07/13/2024 09:00:00', 'Tauchen Sie ein in die Welt der Asteroiden, Kometen und planetaren Kollisionen und erfahren Sie mehr über die beeindruckende Geschichte unseres Sonnensystems.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(7, 'Die Geheimnisse der Schwarzen Löcher', '07/13/2024 15:00:00', 'Eine tiefgehende Erkundung der faszinierenden Phänomene der Schwarzen Löcher und ihrer Auswirkungen auf Raum und Zeit.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(11, 'Kinderplanetarium', '07/14/2024 09:00:00', 'Ein interaktives Erlebnis für die jüngsten Entdecker, um spielerisch die Wunder des Weltraums zu erforschen.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(9, 'Exoplaneten-Expedition', '07/14/2024 15:00:00', 'Begleiten Sie uns auf eine Reise zu den fernen Welten außerhalb unseres Sonnensystems und entdecken Sie potenziell bewohnbare Exoplaneten.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(10, 'Astronomie für Einsteiger', '07/15/2024 09:00:00', 'Eine Einführung in die Grundlagen der Astronomie für Neulinge, die mehr über Sterne, Planeten und den Himmel erfahren möchten.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(10, 'Kunst im Kosmos', '07/15/2024 15:00:00', 'Eine kreative Fusion von Astronomie und Kunst, die die Schönheit des Universums durch visuelle Darstellungen und Projektionen erkundet.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(6, 'Die Geschichte der Raumfahrt', '07/16/2024 09:00:00', 'Eine chronologische Reise durch die Meilensteine der Raumfahrt, von den ersten Satelliten bis zu den aktuellen Marsmissionen.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(8, 'Himmelskonzert', '07/16/2024 15:00:00', 'Genießen Sie eine audiovisuelle Vorführung, bei der Sternbilder und Himmelskörper mit passender Musik harmonisch kombiniert werden.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(6, 'Astronomische R tselrallye', '07/17/2024 09:00:00', 'Ein interaktiver Abend, bei dem die Teilnehmer knifflige astronomische Rätsel lösen und dabei mehr über den Weltraum erfahren.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(7, 'Die Farben des Kosmos', '07/17/2024 15:00:00', 'Eine visuelle Reise, die die verschiedenen Farben im Universum erkundet und erklärt, von leuchtenden Gaswolken bis zu bunten Nebeln.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(7, 'Mars-Expedition live', '07/17/2024 19:00:00', 'Begleiten Sie uns auf eine virtuelle Reise zum Mars und erleben Sie, wie Raumfahrttechnologie diesen fernen Planeten erkundet.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(11, 'Astrofotografie-Workshop', '07/18/2024 09:00:00', 'Lernen Sie die Grundlagen der Astrofotografie und nehmen Sie an einem praktischen Workshop teil, um beeindruckende Himmelsaufnahmen zu erstellen.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(11, 'Die Zukunft der Raumfahrt', '07/18/2024 15:00:00', 'Eine Diskussionsveranstaltung über zukünftige Entwicklungen in der Raumfahrt, von bemannten Marsmissionen bis zu bahnbrechenden Technologien.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(6, 'Sternenreise durch die Galaxie', '07/19/2024 09:00:00', 'Erleben Sie eine faszinierende Reise durch unser Universum, angefangen von den nahen Planeten bis zu den entferntesten Galaxien.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(6, 'Mondnacht im Planetarium', '07/19/2024 15:00:00', 'Eine romantische Nacht unter den Sternen, mit besonderem Fokus auf dem Mond und seinen mystischen Geheimnissen.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(8, 'Kosmische Kollisionen', '07/20/2024 09:00:00', 'Tauchen Sie ein in die Welt der Asteroiden, Kometen und planetaren Kollisionen und erfahren Sie mehr über die beeindruckende Geschichte unseres Sonnensystems.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(7, 'Die Geheimnisse der Schwarzen Löcher', '07/20/2024 15:00:00', 'Eine tiefgehende Erkundung der faszinierenden Phänomene der Schwarzen Löcher und ihrer Auswirkungen auf Raum und Zeit.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(11, 'Kinderplanetarium', '07/21/2024 09:00:00', 'Ein interaktives Erlebnis für die jüngsten Entdecker, um spielerisch die Wunder des Weltraums zu erforschen.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(9, 'Exoplaneten-Expedition', '07/21/2024 15:00:00', 'Begleiten Sie uns auf eine Reise zu den fernen Welten außerhalb unseres Sonnensystems und entdecken Sie potenziell bewohnbare Exoplaneten.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(10, 'Astronomie für Einsteiger', '07/22/2024 09:00:00', 'Eine Einführung in die Grundlagen der Astronomie für Neulinge, die mehr über Sterne, Planeten und den Himmel erfahren möchten.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(10, 'Kunst im Kosmos', '07/22/2024 15:00:00', 'Eine kreative Fusion von Astronomie und Kunst, die die Schönheit des Universums durch visuelle Darstellungen und Projektionen erkundet.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(6, 'Die Geschichte der Raumfahrt', '07/23/2024 09:00:00', 'Eine chronologische Reise durch die Meilensteine der Raumfahrt, von den ersten Satelliten bis zu den aktuellen Marsmissionen.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(8, 'Himmelskonzert', '07/23/2024 15:00:00', 'Genießen Sie eine audiovisuelle Vorführung, bei der Sternbilder und Himmelskörper mit passender Musik harmonisch kombiniert werden.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(6, 'Astronomische R tselrallye', '07/24/2024 09:00:00', 'Ein interaktiver Abend, bei dem die Teilnehmer knifflige astronomische Rätsel lösen und dabei mehr über den Weltraum erfahren.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(7, 'Die Farben des Kosmos', '07/24/2024 15:00:00', 'Eine visuelle Reise, die die verschiedenen Farben im Universum erkundet und erklärt, von leuchtenden Gaswolken bis zu bunten Nebeln.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(7, 'Mars-Expedition live', '07/24/2024 19:00:00', 'Begleiten Sie uns auf eine virtuelle Reise zum Mars und erleben Sie, wie Raumfahrttechnologie diesen fernen Planeten erkundet.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(11, 'Astrofotografie-Workshop', '07/25/2024 09:00:00', 'Lernen Sie die Grundlagen der Astrofotografie und nehmen Sie an einem praktischen Workshop teil, um beeindruckende Himmelsaufnahmen zu erstellen.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(11, 'Die Zukunft der Raumfahrt', '07/25/2024 15:00:00', 'Eine Diskussionsveranstaltung über zukünftige Entwicklungen in der Raumfahrt, von bemannten Marsmissionen bis zu bahnbrechenden Technologien.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(6, 'Reise durch das Sonnensystem', '08/01/2024 10:00:00', 'Begleiten Sie uns auf eine spannende Reise durch unser Sonnensystem und entdecken Sie die faszinierenden Planeten und ihre Monde.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(7, 'Faszination der Sterne', '08/01/2024 14:00:00', 'Erleben Sie die Schönheit und die Geheimnisse der Sterne, von ihrer Geburt bis zu ihrem spektakulären Ende.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(8, 'Die Ringe des Saturn', '08/02/2024 09:00:00', 'Eine detaillierte Betrachtung des beeindruckenden Ringsystems des Saturn und seiner Bedeutung für die Astronomie.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(9, 'Asteroiden und Meteoriten', '08/02/2024 13:00:00', 'Erfahren Sie mehr über die Herkunft, Zusammensetzung und den Einfluss von Asteroiden und Meteoriten auf die Erde.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(10, 'Die Magie des Polarlichts', '08/03/2024 11:00:00', 'Lassen Sie sich von den atemberaubenden Farben und Formen des Polarlichts verzaubern und lernen Sie die wissenschaftlichen Hintergründe kennen.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(11, 'Die Milchstraße entdecken', '08/03/2024 15:00:00', 'Eine Entdeckungsreise durch unsere Heimatgalaxie, die Milchstraße, und ihre zahlreichen Geheimnisse und Wunder.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(6, 'Die Geheimnisse des Mars', '08/04/2024 09:00:00', 'Erforschen Sie den Roten Planeten, seine Landschaften, Atmosphäre und die neuesten Erkenntnisse über die Möglichkeit von Leben auf dem Mars.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(7, 'Sterne und Planeten für Kinder', '08/04/2024 14:00:00', 'Eine kindgerechte Einführung in die Welt der Astronomie, speziell für unsere jungen Besucher.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(8, 'Die Geheimnisse der Dunklen Materie', '08/05/2024 10:00:00', 'Tauchen Sie ein in die mysteriöse Welt der Dunklen Materie und ihre Auswirkungen auf das Universum.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(9, 'Der Tanz der Galaxien', '08/05/2024 16:00:00', 'Erleben Sie die faszinierenden Wechselwirkungen zwischen Galaxien und die daraus resultierenden kosmischen Phänomene.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(10, 'Sonneneruptionen und ihre Auswirkungen', '08/06/2024 11:00:00', 'Erfahren Sie mehr über die gewaltigen Eruptionen auf der Sonne und ihre Auswirkungen auf das Leben auf der Erde.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(11, 'Planeten in fremden Sonnensystemen', '08/06/2024 14:00:00', 'Eine spannende Erkundung der Exoplaneten und der Möglichkeit von Leben in anderen Teilen der Galaxie.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(6, 'Die Geburt und der Tod der Sterne', '08/07/2024 09:00:00', 'Verfolgen Sie den Lebenszyklus der Sterne von ihrer Entstehung in Nebeln bis zu ihrem spektakulären Ende als Supernova oder Schwarzes Loch.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(7, 'Der Mond und seine Mysterien', '08/07/2024 15:00:00', 'Eine ausführliche Betrachtung unseres nächsten Nachbarn im All und die vielen Mythen und wissenschaftlichen Erkenntnisse über den Mond.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(8, 'Die Reise eines Photons', '08/08/2024 10:00:00', 'Verfolgen Sie die unglaubliche Reise eines Lichtteilchens von der Oberfläche der Sonne bis zu seinem Eintreffen auf der Erde.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(9, 'Kosmische Nebel', '08/08/2024 13:00:00', 'Entdecken Sie die prächtigen und geheimnisvollen Nebel im Universum und ihre Rolle in der Sternentstehung.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(10, 'Einstein und die Relativitätstheorie', '08/09/2024 11:00:00', 'Eine Einführung in die revolutionären Ideen von Albert Einstein und ihre Bedeutung für unser Verständnis des Universums.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(11, 'Schwarze Löcher und Wurmlöcher', '08/09/2024 15:00:00', 'Erkunden Sie die faszinierenden Konzepte von Schwarzen Löchern und Wurmlöchern und ihre möglichen Auswirkungen auf Raum und Zeit.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(6, 'Unsere kosmische Nachbarschaft', '08/10/2024 09:00:00', 'Lernen Sie die Sterne und Planeten in unserer unmittelbaren Nachbarschaft kennen und verstehen Sie ihre Bedeutung für die Astronomie.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(7, 'Galaktische Supernovae', '08/10/2024 14:00:00', 'Erleben Sie die gewaltigen Explosionen von Supernovae und ihre Rolle in der Verbreitung von schweren Elementen im Universum.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(8, 'Die Entstehung des Universums', '08/11/2024 10:00:00', 'Eine Reise zurück in die Zeit zu den Anfängen des Universums und die Theorien über den Urknall und die Evolution des Kosmos.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(9, 'Sterne und ihre Konstellationen', '08/11/2024 13:00:00', 'Lernen Sie die wichtigsten Sternbilder am Nachthimmel kennen und die Mythen und Geschichten, die sich um sie ranken.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(10, 'Die Suche nach extraterrestrischem Leben', '08/12/2024 11:00:00', 'Erfahren Sie mehr über die wissenschaftlichen Bemühungen, außerirdisches Leben zu finden und die neuesten Entdeckungen in diesem aufregenden Forschungsfeld.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(11, 'Kosmische Hintergrundstrahlung', '08/12/2024 15:00:00', 'Eine tiefgehende Untersuchung der kosmischen Hintergrundstrahlung und ihrer Bedeutung für unser Verständnis des Universums.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(6, 'Der Einfluss der Sonne auf die Erde', '08/13/2024 09:00:00', 'Entdecken Sie die vielfältigen Wege, wie die Sonne das Leben auf der Erde beeinflusst und prägt.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(7, 'Galaxien und ihre Geheimnisse', '08/13/2024 14:00:00', 'Eine spannende Erkundung der verschiedenen Arten von Galaxien und der faszinierenden Phänomene, die sie enthalten.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(8, 'Die Zukunft des Universums', '08/14/2024 10:00:00', 'Spekulieren Sie über die Zukunft des Universums und die möglichen Szenarien, die auf uns zukommen könnten.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(9, 'Wunder des tiefen Weltraums', '08/14/2024 13:00:00', 'Tauchen Sie ein in die Wunder des tiefen Weltraums und entdecken Sie die faszinierenden Objekte und Phänomene jenseits unseres Sonnensystems.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(10, 'Astronomie für Anfänger', '08/15/2024 11:00:00', 'Einsteigerkurs in die Astronomie, der die Grundlagen und die wichtigsten Konzepte und Beobachtungstechniken erklärt.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(11, 'Die Physik der schwarzen Löcher', '08/15/2024 15:00:00', 'Eine tiefgehende Erkundung der Physik und Mathematik hinter den faszinierenden Phänomenen der schwarzen Löcher.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(6, 'Der Mars-Rover und seine Missionen', '08/16/2024 09:00:00', 'Erfahren Sie mehr über die spannenden Missionen der Mars-Rover und die erstaunlichen Entdeckungen, die sie gemacht haben.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(7, 'Das Rätsel der Dunklen Energie', '08/16/2024 14:00:00', 'Tauchen Sie ein in das größte Rätsel der modernen Astronomie - die Dunkle Energie und ihre Auswirkungen auf das Universum.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(8, 'Der Nachthimmel im Sommer', '08/17/2024 10:00:00', 'Eine Einführung in die schönsten und interessantesten Objekte, die Sie im Sommer am Nachthimmel beobachten können.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(9, 'Astronomische Instrumente', '08/17/2024 13:00:00', 'Lernen Sie die verschiedenen Instrumente kennen, die Astronomen verwenden, um den Himmel zu erforschen.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(10, 'Der große Wagen und seine Geheimnisse', '08/18/2024 11:00:00', 'Entdecken Sie die Geheimnisse des berühmten Sternbildes Großer Wagen und seine Bedeutung in verschiedenen Kulturen.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(11, 'Die Entdeckung der Exoplaneten', '08/18/2024 15:00:00', 'Erfahren Sie mehr über die aufregenden Entdeckungen von Planeten außerhalb unseres Sonnensystems und ihre Bedeutung für die Astronomie.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(6, 'Der Kuipergürtel und seine Bewohner', '08/19/2024 09:00:00', 'Eine spannende Erkundung des Kuipergürtels und der faszinierenden Objekte, die in dieser fernen Region unseres Sonnensystems liegen.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(7, 'Sternschnuppen und Meteorströme', '08/19/2024 14:00:00', 'Erleben Sie die magischen Nächte der Sternschnuppen und erfahren Sie mehr über ihre Herkunft und Bedeutung.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(8, 'Die Geheimnisse der Andromeda-Galaxie', '08/20/2024 10:00:00', 'Eine faszinierende Reise zur Andromeda-Galaxie, unserer nächsten großen Nachbargalaxie, und ihre spannenden Geheimnisse.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(9, 'Der Einfluss des Mondes auf die Erde', '08/20/2024 13:00:00', 'Erfahren Sie mehr über die vielfältigen Einflüsse des Mondes auf das Leben auf der Erde, von den Gezeiten bis zu den biologischen Rhythmen.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(10, 'Supernovae und ihre Überreste', '08/21/2024 11:00:00', 'Erleben Sie die gewaltigen Explosionen von Supernovae und die faszinierenden Überreste, die sie hinterlassen.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(11, 'Das Leben eines Sterns', '08/21/2024 15:00:00', 'Verfolgen Sie die erstaunliche Lebensgeschichte eines Sterns von seiner Geburt in einem Nebel bis zu seinem Ende.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(6, 'Die Milchstraße und ihre Struktur', '08/22/2024 09:00:00', 'Eine tiefgehende Untersuchung der Struktur und der verschiedenen Bestandteile unserer Heimatgalaxie, der Milchstraße.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(7, 'Die großen Teleskope der Welt', '08/22/2024 14:00:00', 'Erfahren Sie mehr über die beeindruckenden Teleskope auf der ganzen Welt und die Entdeckungen, die sie ermöglicht haben.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(8, 'Die Entstehung der Planeten', '08/23/2024 10:00:00', 'Eine detaillierte Betrachtung der Prozesse, die zur Entstehung der Planeten in unserem Sonnensystem geführt haben.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(9, 'Die faszinierende Welt der Kometen', '08/23/2024 13:00:00', 'Erleben Sie die spektakulären Erscheinungen der Kometen und ihre Rolle in der Geschichte und Wissenschaft.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(10, 'Der Einfluss der Dunklen Materie', '08/24/2024 11:00:00', 'Tauchen Sie ein in die Geheimnisse der Dunklen Materie und ihre Auswirkungen auf die Struktur und Entwicklung des Universums.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(11, 'Das Universum und die Quantenmechanik', '08/24/2024 15:00:00', 'Eine Einführung in die erstaunliche Welt der Quantenmechanik und ihre Bedeutung für das Verständnis des Universums.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(6, 'Die kosmische Hintergrundstrahlung', '08/25/2024 09:00:00', 'Erfahren Sie mehr über die Entdeckung und Bedeutung der kosmischen Hintergrundstrahlung und ihre Rolle in der Kosmologie.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(7, 'Die Astronomie der alten Kulturen', '08/25/2024 14:00:00', 'Eine Reise durch die Astronomie der alten Kulturen und ihre beeindruckenden Kenntnisse und Beobachtungen.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(8, 'Die Suche nach Leben im All', '08/26/2024 10:00:00', 'Erfahren Sie mehr über die aktuellen Bemühungen und Technologien, die eingesetzt werden, um außerirdisches Leben zu finden.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(9, 'Der Lebenszyklus der Sterne', '08/26/2024 13:00:00', 'Verfolgen Sie den Lebenszyklus der Sterne von ihrer Entstehung bis zu ihrem Ende als Neutronenstern oder Schwarzes Loch.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(10, 'Kosmische Kollisionen', '08/27/2024 11:00:00', 'Erleben Sie die dramatischen Kollisionen zwischen Himmelskörpern und ihre Auswirkungen auf das Universum.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(11, 'Die Rolle der Gravitation', '08/27/2024 15:00:00', 'Erfahren Sie mehr über die zentrale Rolle der Gravitation in der Struktur und Entwicklung des Universums.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(6, 'Sterne beobachten für Anfänger', '08/28/2024 09:00:00', 'Ein praktischer Workshop für Anfänger, um die Sterne und Sternbilder am Nachthimmel zu erkennen und zu beobachten.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(7, 'Die Wunder des Weltalls', '08/28/2024 14:00:00', 'Eine faszinierende Reise durch die Wunder des Weltalls und die neuesten Entdeckungen der Astronomie.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(8, 'Die Entstehung der Galaxien', '08/29/2024 10:00:00', 'Erfahren Sie mehr über die Entstehung und Entwicklung der Galaxien und die faszinierenden Prozesse, die dabei ablaufen.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(9, 'Das kosmische Netz', '08/29/2024 13:00:00', 'Eine Erkundung des kosmischen Netzes und der großräumigen Struktur des Universums.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(10, 'Die Rolle der Dunklen Energie', '08/30/2024 11:00:00', 'Erfahren Sie mehr über die geheimnisvolle Dunkle Energie und ihre Auswirkungen auf die Expansion des Universums.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(11, 'Der Einfluss des Jupiter auf das Sonnensystem', '08/30/2024 15:00:00', 'Eine Untersuchung der Rolle des Jupiter in unserem Sonnensystem und seine Einflüsse auf andere Planeten und Asteroiden.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(6, 'Das Universum und die Relativitätstheorie', '08/31/2024 09:00:00', 'Eine Einführung in die Relativitätstheorie und ihre Auswirkungen auf unser Verständnis des Universums.');
INSERT INTO ASTROSPHERE.VERANSTALTUNG(RAUM_ID, NAME, DATUM, BESCHREIBUNG) VALUES
(7, 'Die Erforschung der Venus', '08/31/2024 14:00:00', 'Erfahren Sie mehr über die geheimnisvolle Venus, ihre Atmosphäre und die spannenden Missionen, die sie erforscht haben.');



--
-- Inserting data into table ASTROSPHERE.BESTELLUNG
--
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(NULL, 7, 2, 100, 0.8, 3.95);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(28, NULL, 1, 50, 1, 1.71);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(NULL, 21, 7, 65, 0.03, 1.21);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(26, NULL, 2, 105, NULL, 7.86);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(NULL, 1, 9, 75, 0.48, 0.04);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(24, NULL, 10, 95, NULL, 7.38);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(4, NULL, 6, 130, NULL, 7.77);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(12, NULL, 8, 200, NULL, 0.22);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(4, NULL, 7, 500, NULL, 6.64);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(NULL, 11, 6, 293, 1, 3.56);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(NULL, 23, 8, 145, 0.05, 0.92);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(14, NULL, 6, 200, 0.5, 0.77);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(18, NULL, 3, 95, NULL, 2.07);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(NULL, 15, 10, 5, 0.71, 2.15);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(NULL, 13, 3, 15, 1, 5.82);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(NULL, 19, 7, 60, 0.21, 2.5);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(18, NULL, 3, 300, NULL, 2.63);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(NULL, 15, 8, 55, NULL, 4.88);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(NULL, 25, 2, 258, 0.86, 5.75);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(8, NULL, 5, 55, 1, 1.14);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(NULL, 33, 1, 26, 1, 2.54);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(4, NULL, 6, 204, 0.97, 6.39);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(NULL, 7, 8, 56, 0.84, 1.5);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(NULL, 13, 2, 24, 0.41, 2.92);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(12, NULL, 4, 500, NULL, 0.56);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(NULL, 13, 7, 200, 0.28, 7.41);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(2, NULL, 4, 45, 0.29, 3.72);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(NULL, 1, 5, 100, NULL, 3.2);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(4, NULL, 2, 3, 1, 2.96);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(NULL, 27, 1, 256, NULL, 3.19);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(NULL, 37, 2, 25, NULL, 8.04);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(2, NULL, 4, 99, 1, 3.68);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(NULL, 19, 7, 78, 0.01, 1.8);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(4, NULL, 9, 100, 0.87, 2.52);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(NULL, 21, 7, 260, NULL, 7.41);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(2, NULL, 4, 20, NULL, 0.03);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(NULL, 29, 4, 50, 0.55, 6.22);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(4, NULL, 10, 60, 1, 2.98);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(NULL, 31, 6, 55, NULL, 2.13);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(28, NULL, 4, 75, NULL, 2.23);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(20, NULL, 5, 86, 0.45, 6.99);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(NULL, 37, 4, 120, NULL, 4.95);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(22, NULL, 9, 90, NULL, 2.48);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(NULL, 39, 10, 65, NULL, 0.06);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(16, NULL, 3, 39, NULL, 6.08);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(NULL, 29, 5, 46, NULL, 5.19);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(NULL, 23, 7, 50, NULL, 1.43);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(26, NULL, 7, 43, NULL, 4.29);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(6, NULL, 8, 75, NULL, 1.3);
INSERT INTO ASTROSPHERE.BESTELLUNG(SNACK_ID, MERCHARTIKEL_ID, LIEFERANT_ID, ANZAHL, RABATT, ANKAUF_PREIS) VALUES
(NULL, 15, 5, 100, NULL, 6.48);


--
-- Inserting data into table ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER
--
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(7, 11);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(9, 9);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(8, 9);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(4, 4);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(8, 10);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(10, 14);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(5, 9);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(8, 12);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(6, 10);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(3, 5);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(3, 4);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(9, 10);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(2, 6);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(4, 5);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(10, 11);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(9, 13);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(5, 6);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(7, 10);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(3, 7);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(1, 3);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(9, 11);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(8, 11);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(10, 10);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(6, 7);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(5, 5);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(1, 2);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(4, 6);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(10, 12);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(5, 7);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(2, 4);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(4, 8);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(6, 6);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(1, 4);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(9, 12);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(6, 8);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(2, 5);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(7, 8);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(2, 3);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(1, 1);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(4, 7);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(10, 13);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(7, 9);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(3, 6);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(7, 7);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(5, 8);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(1, 5);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(6, 9);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(2, 2);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(8, 8);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_ANGESTELLTER(VERANSTALTUNG_ID, ANGESTELLTER_ID) VALUES
(3, 3);


--
-- Inserting data into table ASTROSPHERE.VERANSTALTUNG_MEDIUM
--
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(7, 11);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(9, 9);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(8, 9);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(4, 4);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(8, 10);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(10, 14);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(5, 9);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(8, 12);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(6, 10);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(3, 5);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(3, 4);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(9, 10);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(2, 6);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(4, 5);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(10, 11);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(9, 13);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(5, 6);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(7, 10);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(3, 7);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(1, 3);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(9, 11);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(8, 11);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(10, 10);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(6, 7);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(5, 5);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(1, 2);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(4, 6);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(10, 12);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(5, 7);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(2, 4);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(4, 8);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(6, 6);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(1, 4);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(9, 12);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(6, 8);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(2, 5);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(7, 8);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(2, 3);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(1, 1);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(4, 7);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(10, 13);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(7, 9);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(3, 6);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(7, 7);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(5, 8);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(1, 5);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(6, 9);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(2, 2);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(8, 8);
INSERT INTO ASTROSPHERE.VERANSTALTUNG_MEDIUM(VERANSTALTUNG_ID, MEDIUM_ID) VALUES
(3, 3);


--
-- Inserting data into table ASTROSPHERE.VERKAUF_MERCH
--
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(47, 21, 1);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(9, 9, 2);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(18, 17, 3);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(4, 3, 4);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(28, 7, 5);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(50, 11, 6);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(45, 13, 7);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(48, 19, 8);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(46, 15, 9);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(23, 13, 10);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(13, 3, 11);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(19, 19, 12);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(42, 5, 13);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(14, 25, 14);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(20, 23, 15);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(49, 11, 16);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(15, 15, 17);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(37, 17, 18);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(43, 13, 19);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(21, 27, 20);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(29, 29, 19);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(38, 37, 18);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(10, 11, 17);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(16, 19, 16);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(5, 5, 15);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(11, 11, 14);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(24, 33, 13);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(30, 35, 12);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(25, 25, 11);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(22, 29, 10);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(44, 39, 9);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(6, 5, 8);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(31, 1, 7);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(39, 3, 6);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(26, 5, 5);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(32, 11, 4);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(17, 17, 3);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(12, 13, 2);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(1, 1, 1);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(34, 1, 2);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(40, 21, 6);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(27, 3, 5);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(33, 31, 8);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(7, 7, 3);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(35, 5, 4);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(41, 7, 7);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(36, 7, 2);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(2, 5, 8);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(8, 9, 3);
INSERT INTO ASTROSPHERE.VERKAUF_MERCH(VERKAUF_ID, MERCHARTIKEL_ID, ANZAHL) VALUES
(3, 13, 3);


--
-- Inserting data into table ASTROSPHERE.VERKAUF_SNACK
--
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(1, 10, 2);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(5, 2, 1);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(30, 14, 4);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(13, 8, 1);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(28, 30, 2);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(35, 24, 1);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(15, 26, 3);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(18, 28, 1);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(16, 16, 2);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(13, 22, 3);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(3, 10, 1);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(19, 18, 3);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(45, 12, 2);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(14, 14, 1);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(20, 2, 2);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(39, 18, 3);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(5, 4, 2);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(27, 6, 2);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(43, 14, 2);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(11, 2, 2);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(19, 4, 2);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(8, 8, 2);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(10, 10, 1);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(46, 6, 2);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(35, 16, 2);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(11, 18, 3);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(24, 14, 2);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(30, 24, 3);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(15, 12, 2);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(2, 22, 1);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(44, 26, 2);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(6, 6, 1);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(31, 28, 2);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(39, 8, 1);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(16, 2, 3);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(3, 2, 1);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(17, 8, 2);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(42, 12, 2);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(14, 4, 2);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(44, 6, 1);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(40, 16, 2);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(27, 18, 5);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(31, 26, 4);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(47, 14, 2);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(35, 30, 2);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(41, 2, 3);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(22, 14, 2);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(48, 8, 2);
INSERT INTO ASTROSPHERE.VERKAUF_SNACK(VERKAUF_ID, SNACK_ID, ANZAHL) VALUES
(3, 12, 1);


--
-- Inserting data into table ASTROSPHERE.VERMIETUNG_RAUM
--
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(9, 7, '07/02/2023 00:00:00', 6);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(9, 9, '02/20/2024 00:00:00', 2);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(18, 18, '03/03/2023 00:00:00', 7);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(4, 4, '02/03/2024 00:00:00', 3);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(9, 8, '10/05/2023 00:00:00', 5);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(12, 10, '02/06/2024 00:00:00', 7);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(7, 5, '07/02/2023 00:00:00', 6);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(10, 8 ,'01/08/2023 00:00:00', 3);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(8, 6, '02/09/2024 00:00:00', 7);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(4, 3,'05/10/2023 00:00:00', 6);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(13, 13, '06/11/2024 00:00:00', 6);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(19, 19, '12/12/2023 00:00:00', 4);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(4, 2, '11/01/2023 00:00:00', 4);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(14, 14, '10/02/2024 00:00:00', 3);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(20, 20, '03/03/2023 00:00:00', 4);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(11, 9, '02/04/2023 00:00:00', 5);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(15, 15, '05/05/2023 00:00:00', 7);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(18, 17, '02/06/2024 00:00:00', 5);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(5, 3, '10/07/2023 00:00:00', 3);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(2, 1, '02/08/2023 00:00:00', 5);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(10, 9, '07/09/2023 00:00:00', 2);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(19, 18, '12/10/2023 00:00:00', 1);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(10, 10, '05/11/2024 00:00:00', 4);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(16, 16, '08/12/2023 00:00:00', 3);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(5, 5, '09/01/2024 00:00:00', 2);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(11, 11, '11/02/2023 00:00:00', 6);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(5, 4, '07/03/2023 00:00:00', 7);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(11, 10, '09/04/2024 00:00:00', 4);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(6, 5, '02/05/2023 00:00:00', 3);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(3, 2, '05/06/2023 00:00:00', 6);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(6, 4, '07/07/2024 00:00:00', 5);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(6, 6, '09/08/2023 00:00:00', 7);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(12, 11, '12/09/2024 00:00:00', 6);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(20, 19, '12/10/2023 00:00:00', 4);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(7, 6, '12/11/2023 00:00:00', 1);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(13, 12, '03/12/2024 00:00:00', 2);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(17, 17, '04/01/2023 00:00:00', 3);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(12, 12, '05/02/2024 00:00:00', 3);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(1, 1, '06/03/2024 00:00:00', 4);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(15, 14, '08/04/2023 00:00:00', 6);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(21, 20, '09/05/2024 00:00:00', 3);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(8, 7, '10/06/2023 00:00:00', 4);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(14, 13, '11/07/2023 00:00:00', 4);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(7, 7, '12/08/2024 00:00:00', 7);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(16, 15, '05/09/2023 00:00:00', 7);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(3, 1, '06/10/2024 00:00:00', 7);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(17, 16, '07/11/2023 00:00:00', 5);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(2, 2, '08/12/2024 00:00:00', 5);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(8, 8, '03/01/2023 00:00:00', 6);
INSERT INTO ASTROSPHERE.VERMIETUNG_RAUM(KUNDE_ID, RAUM_ID, DATUM, DAUER_TAGE) VALUES
(3, 3, '09/02/2024 00:00:00', 7);


--
-- Inserting data into table ASTROSPHERE.VERMIETUNG_TELESKOP
--
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(11, 2, '03/17/2023 00:00:00', 3);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(6, 3, '05/01/2023 00:00:00', 2);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(8, 3, '09/28/2023 00:00:00', 1);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(14, 5, '07/14/2023 00:00:00', 7);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(13, 5, '04/05/2023 00:00:00', 5);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(12, 3, '12/19/2023 00:00:00', 3);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(10, 1, '06/09/2023 00:00:00', 2);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(7, 3, '02/27/2024 00:00:00', 6);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(5, 3, '10/15/2023 00:00:00', 4);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(10, 2, '03/01/2023 00:00:00', 1);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(8, 5, '07/07/2023 00:00:00', 3);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(7, 5, '12/02/2023 00:00:00', 6);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(9, 2, '08/14/2023 00:00:00', 4);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(11, 3, '05/29/2023 00:00:00', 1);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(5, 1, '11/21/2023 00:00:00', 7);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(10, 3, '06/22/2023 00:00:00', 3);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(6, 5, '02/12/2024 00:00:00', 2);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(4, 1, '12/26/2023 00:00:00', 6);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(5, 5, '09/06/2023 00:00:00', 4);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(3, 1, '04/27/2023 00:00:00', 1);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(10, 5, '08/02/2023 00:00:00', 5);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(9, 5, '05/15/2023 00:00:00', 3);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(6, 2, '01/04/2024 00:00:00', 2);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(2, 1, '03/05/2024 00:00:00', 2);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(7, 1, '10/30/2023 00:00:00', 4);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(6, 1, '04/23/2024 00:00:00', 7);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(8, 2, '12/08/2023 00:00:00', 5);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(5, 2, '09/26/2023 00:00:00', 3);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(4, 2, '06/15/2023 00:00:00', 2);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(1, 1, '02/03/2024 00:00:00', 6);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(12, 5, '01/12/2024 00:00:00', 7);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(7, 2, '03/04/2023 00:00:00', 1);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(9, 3, '11/22/2023 00:00:00', 5);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(3, 2, '07/09/2023 00:00:00', 3);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(11, 5, '04/30/2024 00:00:00', 2);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(9, 1, '12/14/2023 00:00:00', 6);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(8, 1, '08/26/2023 00:00:00', 4);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(2, 2, '05/09/2023 00:00:00', 1);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(4, 3, '11/28/2023 00:00:00', 7);
INSERT INTO ASTROSPHERE.VERMIETUNG_TELESKOP(KUNDE_ID, TELESKOP_ID, DATUM, DAUER_TAGE) VALUES
(3, 3, '10/16/2023 00:00:00', 5);

COMMIT;
"""
