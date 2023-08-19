<?php

interface InscriptionInterface{
    public function getDateCreated(): DateTime;
    public function setDateCreated(DateTime $datetime): void;
}